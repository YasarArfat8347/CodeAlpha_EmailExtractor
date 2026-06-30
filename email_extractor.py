import re

def extract_emails(input_filename, output_filename):
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
       
        extracted_emails = re.findall(email_pattern, content)
        
        
        print("🎯 Extracted Emails:")
        if extracted_emails:
            for email in extracted_emails:
                print(f"✅ {email}")
        else:
            print("❌ No emails found in the file.")
            return

       
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for email in extracted_emails:
                output_file.write(email + '\n')
                
        print(f"\n💾 Successfully saved to '{output_filename}'!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found. Please make sure it exists in the same folder.")


extract_emails('input.txt', 'extracted_emails.txt')