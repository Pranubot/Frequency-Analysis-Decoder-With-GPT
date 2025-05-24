import os
import collections
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_frequency(text):
    """Analyze the frequency of letters in the text and return them as a formatted string."""
    # Count only letters, convert to lowercase
    letters = [c.lower() for c in text if c.isalpha()]
    total_letters = len(letters)
    
    if total_letters == 0:
        return "No letters found in text"
    
    # Count frequencies and calculate percentages
    freq = collections.Counter(letters)
    freq_percentages = {char: (count/total_letters*100) for char, count in freq.items()}
    
    # Sort by percentage (highest to lowest)
    sorted_freq = sorted(freq_percentages.items(), key=lambda x: (-x[1], x[0]))
    
    # Format as a readable percentage list
    freq_str = "Letter frequency distribution:\n"
    freq_str += "------------------------\n"
    for char, pct in sorted_freq:
        freq_str += f"{char.upper()}: {pct:.1f}%\n"
    
    # Add total letter count
    freq_str += f"\nTotal letters analyzed: {total_letters}"
    return freq_str

def decode_with_gpt(text, frequencies):
    """Use GPT to decode the text using frequency analysis."""
    try:
        print("Analyzing text with GPT...")
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """You are an expert cryptanalyst specializing in substitution ciphers.
                Your task is to decrypt text that has been encrypted using a simple substitution cipher.
                Use the letter frequency percentages provided to help identify letter substitutions.
                Standard English letter frequencies for reference:
                E: 12.7%, T: 9.1%, A: 8.2%, O: 7.5%, I: 7.0%, N: 6.7%, S: 6.3%,
                H: 6.1%, R: 6.0%, D: 4.3%, L: 4.0%, C: 2.8%, U: 2.8%, M: 2.4%,
                W: 2.4%, F: 2.2%, G: 2.0%, Y: 2.0%, P: 1.9%, B: 1.5%, V: 1.0%,
                K: 0.8%, J: 0.15%, X: 0.15%, Q: 0.10%, Z: 0.07%"""},
                {"role": "user", "content": f"""Please decrypt this substitution cipher text.

ENCRYPTED TEXT:
{text}

FREQUENCY ANALYSIS:
{frequencies}

Using the letter frequencies above and comparing them to standard English letter frequencies, decrypt the text.
No need to show your reasoning, just the final answer with a brief explanation. If you can't decrypt it, just say so."""}
            ],
            temperature=0.7,
            max_tokens=16000
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"ERROR COMMUNICATING WITH GPT: {str(e)}"

def decode_text(encrypted_text):
    """Main function to decode the text."""
    print("\n=== DECODING PROCESS ===")
    print("Original text:", encrypted_text)
    
    print("\nCalculating letter frequencies...")
    frequencies = analyze_frequency(encrypted_text)
    print("\nFrequency Analysis:")
    print(frequencies)
    
    print("\nDecoding with GPT...")
    gpt_analysis = decode_with_gpt(encrypted_text, frequencies)
    print("\nGPT Analysis and Solution:")
    print(gpt_analysis)
    
    return gpt_analysis

if __name__ == "__main__":
    while True:
        # Had trouble with large inputs, so cursor helped me with this solution
        print("\n=== Frequency Analysis Decoder ===")
        print("Enter or paste the encrypted text below (or type 'quit' to exit)")
        print("After pasting, press Enter, then Ctrl+Z (Windows) or Ctrl+D (Unix), then Enter again:")
        
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
            except KeyboardInterrupt:
                print("\nInput cancelled")
                break
        
        encrypted_text = '\n'.join(lines)
        
        if encrypted_text.lower().strip() == 'quit':
            print("Goodbye!")
            break
        elif encrypted_text.strip():
            decode_text(encrypted_text)
        else:
            print("No text entered") 