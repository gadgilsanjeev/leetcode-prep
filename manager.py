import os
import argparse
import glob

# --- Configuration ---
TEMPLATE_PATH = "template.py"
README_PATH = "README.md"
SRC_DIR = "src"

def slugify(text):
    """Converts string to lowercase hyphenated format (e.g., 'Two Sum' -> 'two-sum')."""
    return "-".join(text.lower().split())

def parse_solution_file(filepath):
    """
    Parses the header of a solution file to extract metadata.
    Returns a dict with id, title, difficulty, topic, and relative_path.
    """
    # Skip the template file itself if it's in the src directory
    if os.path.basename(filepath) == "template.py":
        return None

    data = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # Stop parsing at code (docstrings or imports)
                if line.startswith('"""') or line.startswith("from") or line.startswith("import"):
                    break
                if not line.startswith("#"):
                    continue
                
                # Split by the first colon
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.replace("#", "").strip().lower()
                    value = value.strip()
                    
                    # SKIP: If value looks like a placeholder (e.g., "[Problem ID]")
                    if value.startswith("[") and value.endswith("]"):
                        continue
                    
                    data[key] = value
        
        # Fallback: Try to extract ID from filename (e.g., "0001-two-sum.py" -> 1)
        filename = os.path.basename(filepath)
        parts = filename.split("-")
        if parts and parts[0].isdigit():
            data['filename_id'] = int(parts[0])
        else:
            data['filename_id'] = 99999 # Put files without ID at the end
            
        # Calculate relative path for the markdown link
        data['relative_path'] = filepath.replace("\\", "/")
        
        return data

    except Exception as e:
        print(f"⚠️  Warning: Could not parse {filepath}: {e}")
        return None
    
def create_new_problem(id, title, difficulty, topic):
    """Generates a new .py file based on the template."""
    
    # 1. Construct directory and filename
    topic_dir = os.path.join(SRC_DIR, topic.lower().replace(" ", "-"))
    filename = f"{int(id):04d}-{slugify(title)}.py"
    full_path = os.path.join(topic_dir, filename)

    if os.path.exists(full_path):
        print(f"Error: File {full_path} already exists.")
        return

    # 2. Create directory if it doesn't exist
    os.makedirs(topic_dir, exist_ok=True)

    # 3. Read and fill template
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: {TEMPLATE_PATH} not found.")
        return

    with open(TEMPLATE_PATH, 'r') as f:
        content = f.read()

    # Replace placeholders
    content = content.replace("[Problem Title]", title)
    content = content.replace("[Problem ID]", str(id))
    content = content.replace("[Easy/Medium/Hard]", difficulty)
    content = content.replace("[Array, Hash Table, etc.]", topic)
    
    # Optional: Rename 'functionName' to something generic like 'solve' or keep as is
    # content = content.replace("def functionName", "def solve") 

    with open(full_path, 'w') as f:
        f.write(content)

    print(f"✅ Created: {full_path}")
    generate_readme() # Auto-update readme after creating

def generate_readme():
    """Scans the src directory and updates README.md"""
    problems = []
    
    if not os.path.exists(SRC_DIR):
        print("src directory not found.")
        return

    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                data = parse_solution_file(full_path)
                if data:
                    problems.append(data)

    # Safer sorting: Try to use ID from comment, fallback to filename ID
    def get_sort_id(p):
        try:
            # 1. Try 'id' from comment
            if 'id' in p:
                return int(p['id'])
            # 2. Try 'filename_id'
            if 'filename_id' in p:
                return int(p['filename_id'])
        except ValueError:
            pass
        return 99999 # Default if parsing fails

    problems.sort(key=get_sort_id)

    # Build Table Rows
    table_rows = []
    for p in problems:
        pid = p.get('id') or p.get('filename_id')
        title = p.get('title', 'Unknown Title')
        diff = p.get('difficulty', 'Unknown')
        topic = p.get('topics', 'Unknown')
        link = f"[View]({p.get('relative_path')})"
        
        table_rows.append(f"| {pid} | {title} | {diff} | {topic} | {link} |")

    # Construct Full README Content
    header = """# DSA Practice Repository

This repository contains my solutions to algorithmic problems from LeetCode. I use this to sharpen my problem-solving skills and prepare for technical interviews.

## 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📁 Structure
Problems are categorized by topic:
- `arrays` - Problems involving array manipulation.
- `strings` - String parsing and manipulation.
- `hash-table` - Problems optimized using hash maps/sets.

## 📊 Problems Solved

| ID  | Problem | Difficulty | Topic | Link |
|-----|---------|------------|-------|------|
"""
    
    footer = """
---
*Note: Solutions are for educational purposes.*
"""

    with open(README_PATH, 'w') as f:
        f.write(header)
        f.write("\n".join(table_rows))
        f.write("\n")
        f.write(footer)
    
    print(f"✅ README.md updated with {len(problems)} problems.")

# --- CLI Interface ---
def main():
    parser = argparse.ArgumentParser(description="Manage LeetCode Solutions")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Command: New
    parser_new = subparsers.add_parser("new", help="Create a new problem file")
    parser_new.add_argument("id", type=int, help="Problem ID (e.g., 1)")
    parser_new.add_argument("title", type=str, help="Problem Title (e.g., 'Two Sum')")
    parser_new.add_argument("difficulty", type=str, choices=["Easy", "Medium", "Hard"], help="Difficulty")
    parser_new.add_argument("topic", type=str, help="Topic (e.g., 'Array')")

    # Command: Generate Readme
    subparsers.add_parser("readme", help="Regenerate README.md")

    args = parser.parse_args()

    if args.command == "new":
        create_new_problem(args.id, args.title, args.difficulty, args.topic)
    elif args.command == "readme":
        generate_readme()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()