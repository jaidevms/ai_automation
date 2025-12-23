import re

def convert_arff_to_csv(input_file, output_file):
    """Convert ARFF file to proper CSV format"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extract column names from @attribute lines
    columns = []
    data_start_idx = 0
    
    for idx, line in enumerate(lines):
        if line.startswith('@attribute'):
            # Extract attribute name (between quotes or first word after @attribute)
            match = re.search(r"@attribute\s+'([^']+)'", line)
            if match:
                columns.append(match.group(1))
            else:
                match = re.search(r"@attribute\s+(\S+)", line)
                if match:
                    columns.append(match.group(1))
        elif line.strip() == '@data':
            data_start_idx = idx + 1
            break
    
    # Write CSV file
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write(','.join(columns) + '\n')
        
        # Write data rows
        for line in lines[data_start_idx:]:
            if line.strip():  # Skip empty lines
                f.write(line)
    
    print(f"Converted {input_file} -> {output_file}")
    print(f"  Columns: {len(columns)}")
    print(f"  Data rows: {len(lines) - data_start_idx}")

# Convert all three files
convert_arff_to_csv('kdd_test.csv', 'kdd_test_converted.csv')
convert_arff_to_csv('kdd_test21.csv', 'kdd_test21_converted.csv')
convert_arff_to_csv('kdd_train.csv', 'kdd_train_converted.csv')

print("\nAll files converted successfully!")
