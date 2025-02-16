import random
import time
from tqdm import tqdm  

def generate_initial_population(subjects, weekly_constraints, teachers, days, periods_per_day, population_size=100):
    """Generates an initial random population of timetables with teacher assignments."""
    population = []
    for _ in range(population_size):
        schedule = {day: [] for day in days}
        remaining_classes = {subj: weekly_constraints[subj] for subj in subjects}
        
        for day in days:
            available_subjects = list(subjects)
            random.shuffle(available_subjects)
            
            for _ in range(periods_per_day[day]):
                if not available_subjects:
                    available_subjects = list(subjects)
                    random.shuffle(available_subjects)
                
                chosen_subject = random.choice(available_subjects)
                if remaining_classes[chosen_subject] > 0:
                    teacher = teachers[chosen_subject]
                    schedule[day].append((chosen_subject, teacher))
                    remaining_classes[chosen_subject] -= 1
                    available_subjects.remove(chosen_subject)
                else:
                    available_subjects.remove(chosen_subject)
        
        population.append(schedule)
    return population

def fitness(schedule, weekly_constraints):
    """Evaluates the fitness of a schedule."""
    score = 0
    subject_counts = {subj: 0 for subj in weekly_constraints}
    
    for day, periods in schedule.items():
        day_subjects = set()
        for subject, _ in periods:
            subject_counts[subject] += 1
            day_subjects.add(subject)
        score += len(day_subjects)  
    
    for subject, count in subject_counts.items():
        score -= abs(weekly_constraints[subject] - count) * 5  
    
    return score

def crossover(parent1, parent2):
    """Performs crossover to create a new schedule."""
    child = {}
    for day in parent1:
        if random.random() < 0.5:
            child[day] = parent1[day]
        else:
            child[day] = parent2[day]
    return child

def mutate(schedule, subjects, teachers):
    """Randomly mutates a schedule to introduce variation."""
    day = random.choice(list(schedule.keys()))
    if schedule[day]:
        idx = random.randint(0, len(schedule[day]) - 1)
        new_subject = random.choice(subjects)
        schedule[day][idx] = (new_subject, teachers[new_subject])
    return schedule

def genetic_algorithm(subjects, weekly_constraints, teachers, days, periods_per_day, generations=500, population_size=100):
    """Runs the genetic algorithm to optimize the schedule."""
    population = generate_initial_population(subjects, weekly_constraints, teachers, days, periods_per_day, population_size)
    
    for gen in tqdm(range(generations), desc="Generating Timetable", unit="gen"):
        population = sorted(population, key=lambda x: fitness(x, weekly_constraints), reverse=True)
        
        new_population = population[:10]  # Keep top solutions
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:  # Mutation chance
                child = mutate(child, subjects, teachers)
            new_population.append(child)
        
        population = new_population
    
    return sorted(population, key=lambda x: fitness(x, weekly_constraints), reverse=True)[0]

if __name__ == "__main__":
    subjects = ["Bengali", "Math", "English", "History", "Geography", "Life Science", "Physical Science", "Physical Education", "Computer"]
    weekly_constraints = {
        "Bengali": 7,
        "Math": 6,
        "English": 6,
        "History": 5,
        "Geography": 5,
        "Life Science": 6,
        "Physical Science": 6,
        "Physical Education": 6,
        "Computer": 2
    }
    teachers = {
        "Bengali": "RKM",
        "Math": "TS",
        "English": "DKD",
        "History": "SPB",
        "Geography": "NKS",
        "Life Science": "APD",
        "Physical Science": "SP",
        "Physical Education": "TB",
        "Computer": "SKB"
    }
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    periods_per_day = {day: 8 for day in days[:-1]}
    periods_per_day["Saturday"] = 4
    
    best_schedule = genetic_algorithm(subjects, weekly_constraints, teachers, days, periods_per_day)
    
    for day, periods in best_schedule.items():
        print(f"{day}: {', '.join([f'{subj} ({teacher})' for subj, teacher in periods])}")
