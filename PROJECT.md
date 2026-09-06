# knD - knermie's dragons

## Vision

Build a computational platform capable of representing and simulating biological
systems across multiple levels of organization, from genes and proteins through
cells, tissues, organs, and eventually integrated organism physiology.

The long-term goal is to create a virtual organism whose biological systems can
be explored, modified, and simulated computationally.

The project will prioritize scientific accuracy, modularity, reproducibility,
and validation against experimental data.

---

## Core Principles

### 1. Scientific accuracy

Biological claims should be supported by reliable scientific evidence whenever
possible.

The system must distinguish between:

- experimentally established facts
- well-supported scientific models
- computational predictions
- hypotheses
- assumptions
- unknowns

The AI must never present an assumption as an established biological fact.

### 2. Modular architecture

The system should consist of independent modules that can be developed,
tested, replaced, and improved independently.

Potential modules include:

- genetics
- gene regulation
- RNA
- proteins
- protein interactions
- metabolism
- signaling
- cells
- cell populations
- tissues
- organs
- physiology
- organism-level simulation
- scientific literature
- biological databases
- AI reasoning

### 3. Reproducibility

Simulation results should be reproducible.

Important inputs, parameters, model versions, and assumptions should be recorded.

### 4. Validation

Every significant biological model should eventually have validation tests
against known experimental or published results.

A model should not be considered reliable merely because it produces plausible
results.

### 5. Separation of AI and simulation

The AI is responsible for reasoning, interpretation, research, planning, and
interaction with the user.

The simulation engine is responsible for deterministic or explicitly
stochastic biological calculations.

The AI should not replace mathematical or mechanistic models when those models
are appropriate.

### 6. Explicit uncertainty

The system should communicate uncertainty.

Predictions should eventually include confidence or uncertainty information
where scientifically meaningful.

### 7. Version control

All source code should be maintained through Git.

Major changes should be committed with meaningful commit messages.

### 8. Avoid unnecessary complexity

Build the simplest working version first.

Do not implement a sophisticated biological subsystem until a simpler validated
version is working.

---

## Development Philosophy

This project will be developed incrementally.

Do NOT attempt to build a complete virtual animal immediately.

Each layer must be independently useful and testable before moving to the next
layer.

The development hierarchy is approximately:

DNA
↓
Genes
↓
Gene regulation
↓
RNA
↓
Proteins
↓
Protein interactions
↓
Biochemical reactions
↓
Metabolic networks
↓
Cells
↓
Cell populations
↓
Tissues
↓
Organs
↓
Organ systems
↓
Whole-organism physiology

---

## AI Development Team

The project may use multiple AI systems.

### Primary Architect

Responsible for:

- overall architecture
- project planning
- implementation
- integration
- explaining technical concepts
- maintaining consistency across the project

### Software Engineering Reviewer

Responsible for:

- reviewing code
- identifying bugs
- improving architecture
- refactoring
- testing
- identifying technical debt

### Scientific Reviewer

Responsible for:

- evaluating biological assumptions
- checking scientific reasoning
- identifying unsupported claims
- comparing models with scientific literature
- identifying limitations

AI-generated scientific claims must not automatically be treated as correct.

---

## Safety

The initial project is a computational research and simulation platform.

The project should focus on understanding and modeling biological systems
computationally.

Do not treat simulation results as proof that a biological intervention will
work in a real organism.

---

## Current Goal

The immediate goal is NOT to simulate a complete animal.

The immediate goal is to build the software foundation required to eventually
support increasingly sophisticated biological simulations.

The first functional milestone should be a small system that can:

1. represent biological entities
2. store relationships between them
3. retrieve scientific information
4. perform a simple biological simulation
5. explain the simulation results through an AI interface