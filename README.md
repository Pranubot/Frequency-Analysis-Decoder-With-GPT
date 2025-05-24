# Frequency Analysis Decoder with GPT

This Python script decodes monoalphabetic substitution ciphers by analyzing letter frequencies and using OpenAI's GPT-4o-mini model to perform the decryption.

This is an ongoing project and is a WIP. This project is not always accurate gives questionable responses at times, I'll explain why. 
Comparing this to my ROT chiper with GPT, there's a lot more uncertianty about your decryption. For ROTs, you just do the 25 variations and pick the best. For frequency analysis, you really have to do a lot of guess and check. You may be given a sentence that doesn't have the letter 'e', and that will throw off everything. 
That being said, this script relies heavily on GPT and how well it will do on your execution. I've gotten varying results, with GPT getting pretty darn close one time, but giving me pure BS it thought of other times. One example that did work was this one from my cryptography textbook:
```
JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX
```
In the future, I may have the program rely less on Chat GPTs analysis, and have multiple subsitutions done in advance before shipping it off to GPT for it's input.

## Features
- Analyzes letter frequencies in the encrypted text
- Calculates precise percentage distribution for each letter
- Provides GPT with both the encrypted text and frequency analysis
- Uses GPT 4o-mini to attempt decryption by comparing with standard English letter frequencies
- Handles multi-line input for longer encrypted texts

## Requirements
- Python 3.6 or higher
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/pranubot/Frequency-Analysis-Decoder-With-GPT
cd Frequency-Analysis-Decoder-With-GPT
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:
```bash
python decoder.py
```

The script will:
1. Prompt you to enter or paste the encrypted text
2. Analyze letter frequencies and calculate percentages
3. Display a detailed frequency distribution
4. Send both the text and frequency analysis to GPT
5. Return GPT's decryption attempt or explanation

### Input Instructions
- Type or paste your encrypted text
- Press Enter
- Press Ctrl+Z (Windows) or Ctrl+D (Unix)
- Press Enter again

Type 'quit' to exit the program.

## How it works

The script performs a detailed frequency analysis of the encrypted text, calculating the exact percentage of occurrence for each letter. This information, along with the encrypted text, is sent to GPT-4o-mini, which attempts to decrypt the text by:

1. Comparing the frequency distribution with standard English letter frequencies
2. Looking for patterns in the text
3. Using its knowledge of English language structure
4. Providing a decrypted version if possible, or explaining why it couldn't decrypt the text

Standard English letter frequencies used for reference:
- E: 12.7%
- T: 9.1%
- A: 8.2%
- O: 7.5%
- I: 7.0%
- N: 6.7%
- And so on...

