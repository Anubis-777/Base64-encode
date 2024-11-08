# Base64 Encoding Script

This tool helps you encode text using different types of Base64 at multiple levels. It can do standard Base64, URL-safe Base64, and a custom version of Base64. You get to choose how many times you want the text to be encoded.

## How It Works

Base64 encoding takes 24 bits (or 3 bytes) and turns them into four 6-bit Base64 characters. This script lets you see how text changes when you encode it in different ways and multiple times. It's a way to learn what happens to the text after each level of encoding.

## How to Use It

```sh
python encode64multilevel.py [text_to_encode] [number_of_levels]
```

Replace `[text_to_encode]` with the text you want to encode, and `[number_of_levels]` with the number of times you want to encode it.

The script will show different versions of the encoded text, depending on the type of encoding and how many levels you choose.

## Example

```sh
python encode64multilevel.py "HelloWorld" 2
```

This command will encode the text "HelloWorld" two times using each type of Base64 encoding: standard, URL-safe, and custom.

## Output

The script will show the output for each level of encoding like this:
```
<encoding_type> Level <n>: <encoded_string>
```

### Example Output

```
standard Level 1: SGVsbGx8|SGVs|...
standard Level 2: SFxsZ3xVYX|...
urlsafe Level 1: SGVsVGx8|SGVs|...
urlsafe Level 2: SFlfU3xVY3|...
custom Level 1: ...
...
```

## Requirements

- Python version 3 or higher.

## Handling Errors

- The script checks if you entered the needed arguments. If something is missing, it will show you how to use the script.
- If you enter an unknown encoding type, the script will raise a `ValueError`.

## Example Walkthrough

If you want to encode the text "example" using two levels of encoding, you would use the following command:
```sh
python encode64multilevel.py example 2
```

The script will encode the text and print the result for each type of Base64 encoding.

## Contributing

If you have any suggestions or improvements, contributions are welcome! Please open an issue or send a pull request.

This script is based on the original work by [@kerolesgamal58](https://github.com/kerolesgamal58), and the modifications made here are improvements and updates to that original code.

Special thanks to [@kerolesgamal58](https://github.com/kerolesgamal58) for contributions and support.


