# OpenAI Voice Assistant

This is an example of a simple voice AI voice assistant running from a python script. The script waits for the user to ask a question, then converts the question to text and sends this to ChatGPT 3.5. The response is then read back over system audio by gTTP.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

* [Python > 3.9](https://www.python.org/downloads/)
* [ffmpeg](https://ffmpeg.org/download.html)
* [OpenAI API Key](https://openai.com/)

### Installing

1. Edit template.config file to add in the API key and change its name to private.config
```
[SECRETS]
api_key = your_api_key
```
2. Create a virtual environment for the project 
```
python -m venv VoiceAIEnv
```
3. Activate the virtual environment
  ```
  Windows -> .\testEnv\Scripts\activate
  linux -> source testEnv\bin\activate
  ```
4. Install Python packages
  ```
  pip install -r requirements.txt
  ```
5. Add 
  ```
  pip install -r requirements.txt
  ```

### Executing program

1. Run main.py
```
python main.py
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

[Robert Rochlin](https://github.com/rrochlin)

## Version History

* 0.1
    * Initial Release

## Common Issues

* ffmpeg needs to be added to path or else you will get this error from _winapi.CreateProcess
```
FileNotFoundError: [WinError 2] The system cannot find the file specified
```

## License

Copyright (c) 2023 Robert Rochlin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)