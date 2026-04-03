# ADR-0001: Use Python for the initial implementation

## Context

The project needs to extract YouTube transcripts and later evolve into a processing pipeline.

## Decision

Use Python for V0.

## Rationale

Python provides:
- fast implementation
- mature ecosystem
- easy future integration with APIs, workers, and AI tooling

## Consequences

Pros:
- rapid development
- good text-processing ecosystem

Cons:
- not the fastest language for high-performance workloads
