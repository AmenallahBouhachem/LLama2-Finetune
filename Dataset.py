import random
import pandas as pd
# Initialize an empty list to store prompt-response pairs
dataset = []

# Generate 1000 math questions and their responses
for _ in range(1000):
    # Generate random numbers for multiplication
    num1 = random.randint(1, 9999)
    num2 = random.randint(1, 9999)
    L=list()
    # Calculate the answer
    answer = num1 * num2

    # Create the prompt
    prompt = f"What is {num1} * {num2}?"

    # Generate the response using the long multiplication method
    response = f"Here are the steps for multiplying {num1} * {num2} using the long multiplication method.\n"
    num1_str = str(num1)
    num2_str = str(num2)

    for i, digit1 in enumerate(reversed(num1_str)):
        for j, digit2 in enumerate(reversed(num2_str)):
            product = int(digit1) * int(digit2)
            response += f"- {digit1} (from {10**i} place of first number) * {digit2} (from {10**j} place of second number) = {product} -> Shift it {i + j} places to the left to get {product * (10**(i + j))}\n"
            result = product * (10**(i + j))
            L.append(result)
 # Calculate the final sum from the list L
    final_sum = sum(L)

    # Add the sum to the response
    response += f"\nNow, add all these results together:\nThe sum of {', '.join(map(str, L))} = {final_sum}."

    # Append the prompt-response pair to the dataset
    dataset.append({"prompt": prompt, "response": response})

# Print the first row as an example
print("Example:")
print("prompt:")
print(dataset[0]["prompt"])
print("response:")
print(dataset[0]["response"])

# Save the dataset to a file (optional)
df = pd.DataFrame(dataset)

# Save the DataFrame as a CSV file
csv_filename = "multiplication_dataset.csv"
df.to_csv(csv_filename, index=False)
