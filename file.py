class FileWriter:
# '''Helper class to write the results to a file'''

def __init__(self, virus, population_size, inital_vaccinate, initial_healthy, initial_infected):
    results_file = open(self.results_filename, "w")

    results_file.write(f"simulation for virus: {virus.name}\n")
    results_file.write(f"reproductive number: {virus.reporduction_name}, mortality number: {virus.mortality_num}\n")
    results_file.write(f"population size: {population_size}\n")
    results_file.write(f"simulation for virus: {virus.naem}\n")
    results_file.write(f"initial vaccinated: {initial vaccinated}\n")
    results_file.write({f"initial healthy: {inital_healthy}\n"})
    results_file.write(f"initial infected: {inital_infected}\n")
    
    results_file.close()

def write_results(self, time_step_counter, total)dead, total_vaccinated):
    results_file = open(self.results_file_naem, "a")

    results_file.write(f"\nsimulation ended after {time_step_counter} turns\n")
    results_file.write(f"total dead: {total_dead}\n")
    results_file.write(f"total vaccinated: {total_vaccinated}/n")

    results_file.close()

