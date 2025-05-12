import json
from collections import defaultdict

# Load the JSON file
with open("first_1000_studies.json", "r", encoding="utf-8") as file:
    studies = json.load(file)

# Initialize variables
outcome_measure_to_study_ids = defaultdict(list)
primary_outcomes_with_results = []

# Process each study
for study in studies:
    if study.get("hasResults"):  # Check if the study has results
        outcomes_module = study.get("protocolSection", {}).get("outcomesModule", {})
        primary_outcomes = outcomes_module.get("primaryOutcomes", [])
        
        if primary_outcomes:  # Check if primary outcomes exist
            study_id = study.get("protocolSection", {}).get("identificationModule", {}).get("nctId", "Unknown ID")
            
            # Map outcome measures to study IDs
            for outcome in primary_outcomes:
                measure = outcome.get("measure", "Unknown Measure")
                outcome_measure_to_study_ids[measure].append(study_id)
            
            # Append primary outcomes with results
            primary_outcomes_with_results.append({
                "studyId": study_id,
                "primaryOutcomes": primary_outcomes
            })

# Convert the mapping to a list of dictionaries for better readability
detailed_report = [
    {"measure": measure, "studyIds": study_ids}
    for measure, study_ids in outcome_measure_to_study_ids.items()
]

# Save the detailed report to a JSON file
with open("detailed_outcome_measures.json", "w", encoding="utf-8") as output_file:
    json.dump(detailed_report, output_file, indent=4)

# Save the extracted primary outcomes to a JSON file
with open("primary_outcomes_with_results.json", "w", encoding="utf-8") as output_file:
    json.dump(primary_outcomes_with_results, output_file, indent=4)

# Print a message indicating completion
print("Detailed report saved to 'detailed_outcome_measures.json'.")
print("Primary outcomes extracted and saved to 'primary_outcomes_with_results.json'.")