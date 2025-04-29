import re

class ClassCommandParser:
    def __init__(self, input_text):
        self.input_text = input_text.strip()
        self.class_name = ""
        self.fields = []
    
    def parse(self):
        pattern = r"Create a class called (\w+) with fields (.+)"
        match = re.match(pattern, self.input_text)
        if not match:
            raise ValueError("Input does not match expected format.")
        
        self.class_name = match.group(1)
        fields_text = match.group(2)
        self.fields = [field.strip() for field in fields_text.split(",")]
    
    def generate_code(self):
        lines = []
        lines.append(f"class {self.class_name}:")
        lines.append("    def __init__(self, " + ", ".join(self.fields) + "):")
        for field in self.fields:
            lines.append(f"        self.{field} = {field}")
        return "\n".join(lines)

    def save_to_file(self, code):
        filename = f"{self.class_name}.py"
        with open(filename, "w") as f:
            f.write(code)
        print(f"\n✅ Python code successfully saved to {filename}")

# --- Main Program ---
if __name__ == "__main__":
    print("Welcome to the Class Generator!")
    while True:
        input_command = input("\nEnter your command (e.g., Create a class called Student with fields name, GPA, age):\n> ")
        
        try:
            parser = ClassCommandParser(input_command)
            parser.parse()
            output_code = parser.generate_code()
            print("\nGenerated Python Code:\n")
            print(output_code)
            parser.save_to_file(output_code)  # Save the code to a file
            break  # Exit the loop if successful
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please try again following the correct format!")