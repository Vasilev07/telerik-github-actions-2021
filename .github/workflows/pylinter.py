name: Practice
  
on:
  push:
    branches: [ main ]
    paths:
      - 'factorial.py'
      - 'lint_test.py'

job:
  lint:
    runs-on: ubuntu-latest
    steps:
      - name: Prints the os we are running on
        run: echo "This step runs on: ${{ runner.os }}"
      - name: Prints the branch and repo
        run: echo "The branch is: ${{ github.ref }} in repo: ${{ github.repository }}"
      - name: Check out our repo
        uses: actions/checkout@v2
        run: echo "${{ github.repository }} was checkout in the container"
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pyp install pylint
      - name: Run lint
        run: |
          python lint_test.py
      - name: Build container
        run: |
          echo "Building the container..."
          sleep 60
          echo "Docker built sucessfully"
      - name: Deploy
        run: |
          echo "Deploying"
          sleep 60
          echo "Deploied"
