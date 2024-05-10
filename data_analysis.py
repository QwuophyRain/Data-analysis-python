def analyze_data(data):
  """
  Analyzes a list of numeric values and calculates various statistical measures.

  Args:
    data: A list of numeric values.

  Returns:
    A dictionary containing the calculated statistical measures.
  """
  results = {}

  # Calculate mean
  results["mean"] = sum(data) / len(data)

  # Calculate median
  data.sort()
  if len(data) % 2 == 0:
    median = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
  else:
    median = data[len(data) // 2]
  results["median"] = median

  # Calculate mode
  from collections import Counter
  counts = Counter(data)
  most_frequent = counts.most_common(1)
  results["mode"] = most_frequent[0][0] if most_frequent else None

  # Calculate standard deviation
  squared_deviations = [(x - results["mean"])**2 for x in data]
  variance = sum(squared_deviations) / (len(data) - 1)
  results["standard_deviation"] = variance**0.5

  return results

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = analyze_data(data)

print("Mean:", stats["mean"])
print("Median:", stats["median"])
print("Mode:", stats["mode"])
print("Standard deviation:", stats["standard_deviation"])
