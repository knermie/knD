# knD - knermie's dragons
A vibe coded long term project for simulating a biological system on a genetic level of depth

Phase 0 provides a minimal Python package and one CLI test. Running it prints
`knD is running.` Biological simulation code has not been implemented yet.

## Setup (Windows PowerShell)

You need Python 3.11 or newer. Open PowerShell in the project folder and check:

```powershell
python --version
```

Create a virtual environment, which keeps this project's installed packages
separate from other Python projects:

```powershell
python -m venv .venv
```

Activate it in each new terminal session:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project and its test dependency:

```powershell
python -m pip install -e ".[dev]"
```

The `-e` option installs in editable mode: changes under `src/knd/` take effect
without reinstalling. The `[dev]` extra installs pytest, our test framework.
Setuptools is the build tool used during installation. There are no application
runtime dependencies. Initial installation requires access to a package index.

If PowerShell blocks activation, you can use the environment's Python directly
without changing your execution policy:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m knd
.\.venv\Scripts\python.exe -m pytest
```

## Run

After installation, with the environment activated:

```powershell
python -m knd
```

Expected output:

```text
knD is running.
```

## Test and develop

Run tests from the project folder with the environment activated:

```powershell
python -m pytest
```

The single test launches the installed CLI and checks its output and successful
exit. Application code lives in `src/knd/`; automated tests live in `tests/`.
Make a small change, run the application and tests, then review the changes
before committing. To leave the virtual environment, run `deactivate`.

## Usage notice

This repository is for reference only. You may read the code, but you may not copy, modify, or redistribute it.
