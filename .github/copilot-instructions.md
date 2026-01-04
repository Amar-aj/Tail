# Copilot Instructions for Tail.Blazor Repository (Feature Development Guidance)

_Last updated: January 4, 2026_

## Table of Contents
- [Purpose](#purpose)
- [General Rules](#general-rules)
- [Design Principles](#design-principles)
- [Repository Structure](#repository-structure)
- [Component Implementation Guidelines](#component-implementation-guidelines)
- [Testing Requirements](#testing-requirements)
- [Performance & Size Targets](#performance--size-targets)
- [Multi-Framework Targeting](#multi-framework-targeting)
- [Documentation Practices](#documentation-practices)
- [Accessibility](#accessibility)
- [Native AOT Readiness](#native-aot-readiness)
- [CI/CD & Verification](#cicd--verification)
- [Documentation and Catalog Verification](#documentation-and-catalog-verification)
- [Contribution Requirements](#contribution-requirements)
- [Checklist for New Contributions](#checklist-for-new-contributions)

---

## Purpose

These instructions define rules for Copilot and contributors to ensure all code and documentation changes meet the Tail.Blazor project’s technical and architectural standards. This guarantees ongoing compliance with SRS v1.0.0, aligns with component modularity and performance ethos, and supports frictionless development and maintenance.

---

## General Rules

1. **Do not break solution build.** All changes _must_ result in a clean build without warnings or errors in all frameworks (`net8.0`, `net9.0`, `net10.0`).
2. **Ultra-modularity:** _Every individual component_ should remain an independent project and NuGet package.
3. **No new monolithic packages** or tightly coupled “bundles” – only independent or meta-packages.
4. **Keep components lightweight:** Review target sizes for ALL new/modified components. Do NOT exceed `2-8 KB` average per component unless justified and pre-approved.
5. **Consistency:** All code must follow project coding standards, naming conventions, and existing patterns.
6. **Documentation is mandatory** for every new feature, public API, or component.
7. **Tests are mandatory** for all components, with a goal of ≥90% _bUnit_ code coverage for each.
8. **New modules or features** must reference their relevant SRS section(s) in PR descriptions.
9. **Do NOT create any new `.md` documentation files for features, guides, or component listings; always manage component catalogs, documentation status, and feature lists in the _Scope_ page(s) or within the documentation site itself, not standalone Markdown files.**

---

## Design Principles

- **Zero-Waste**: Code only what’s strictly needed. Do NOT add unused code paths, extra dependencies, or scripts.
- **No "side effect" dependencies**: Each component references ONLY the minimal set of required packages.
- **AOT, Trimming, and Tree-Shaking**: All code must be compatible with .NET Trimming and Native AOT. Avoid _reflection_, _dynamic_, or _unsupported APIs_.
- **Framework-agnostic**: Every component must build and run correctly on .NET `8.0`, `9.0`, and `10.0`.

---

## Repository Structure

- Solution file: `Tail.Blazor.sln`
- **Each component lives in its own folder/project** under `src/components/[ComponentName]/`
- Core Base: `src/packages/Tail.Blazor.Core.Base/`
- Theming: `src/packages/Tail.Blazor.Core.Theme/`
- Docs: `src/apps/Tail.Blazor.Docs/`
- Studio: `src/apps/Tail.Blazor.Studio/`
- Tests: All unit tests go into `tests/Tail.Blazor.Tests/`
- Shared build props: `Directory.Build.props`
- SRS/reference: `.github/copilot-instructions.md`, `.github/SRS.md`

---

## Component Implementation Guidelines

- **New Components**: 
  - Must be placed in `src/components/[ComponentName]/`
  - Implementation must be in `.razor` (UI) and `.razor.cs` (logic if needed)
  - All code must compile for all TargetFrameworks
  - Strictly _no stubs_, skeletons, or placeholder components in production branches

- **Public API**:
  - Document all [Parameter], [CascadingParameter], and [EventCallback]s in `<summary>` XML comments
  - Ensure strong typing and null-safety

- **Dependencies**:
  - Reference only Core/Base, Theme, or other atomic package dependencies.
  - Never reference other components unless explicitly required for composite controls (ex: ButtonGroup -> Button)
  - Update conditional dependencies for target frameworks as per build standards.

- **Size Targets**:
  - Average: `2-8 KB` gzipped per component (check on every PR!)
  - Forms, feedback, navigation, icon components should be in 2-8 KB range
  - DataGrid, Chart, or similarly complex controls may be up to 18 KB max

---

## Testing Requirements

- Each component _must_ have unit tests in `tests/Tail.Blazor.Tests/` using [bUnit](https://bunit.dev/)
- ≥90% code coverage required for all public APIs and rendering scenarios
- New/changed components _must_ not decrease current coverage
- CI/CD must run all tests on PRs
- **No test, no merge.**

---

## Performance & Size Targets

- **Component render time:** < 3 ms average; < 6 ms (p95)
- **Bundle size:** 2-8 KB (avg); 18 KB (max) per component
- **JavaScript footprint:** <10 KB total for all components (if possible)
- Use zero-JS/JS Interop _only where absolutely unavoidable_

---

## Multi-Framework Targeting

- All packages/components must define:
  ```xml
  <TargetFrameworks>net8.0;net9.0;net10.0</TargetFrameworks>
  ```
- Use _conditional_ package references for:
  - `Microsoft.AspNetCore.Components`
  - `Microsoft.AspNetCore.Components.Web`
  - `Microsoft.Extensions.DependencyInjection.Abstractions` (core only)
- No TFM-specific logic in source unless strictly necessary and documented
- Docs and Studio apps must also target appropriate frameworks

---

## Documentation Practices

- Every public component/class must be documented in XML comments
- Docs site source: `src/apps/Tail.Blazor.Docs/`
  - Must include clear API, usage, examples
  - Update sidebar/navigation if adding/changing components
- Add new component documentation pages in both `/Components/` and `/Docs/` subfolders as appropriate
- If updating or introducing SRS differences, document in this file and reference in PR description
- **Documentation Scope & Verification**:
  - Identify and report all missing component documentation pages.
  - **Automate this check**: Use a script to enumerate all components, then check for existence of matching doc pages.
  - Update the **Scope** page (`Scope.razor`) in the docs:
    - List every component and every doc page, marking as _exists_ or _missing_.
    - Prefer to update this with a script to guarantee accuracy given project scale.
  - As much as possible, automate updating of all component documentation, references, and inter-package/component/package relationships in the docs.
  - For every doc/site/guide change, update all references, menus, indexes, and cross-links as needed.
  - **Do NOT create new `.md` documentation files for feature guides, component lists, or catalog tracking—manage all such lists and progress tracking in the _Scope_ page of the documentation site, NOT in Markdown files.**

---

## Accessibility

- All visual components must meet or exceed WCAG 2.2 Level AA targets
- Provide ARIA labels and keyboard navigation everywhere applicable
- Test with screen readers and contrast-checking tools before merge
- Document compliance status for every new component (see checklist)

---

## Native AOT Readiness

- Components must pass Native AOT builds—test with `dotnet publish /p:PublishAot=true`
- Avoid use of reflection, dynamic loading, or unsupported APIs
- Report and fix any AOT errors promptly

---

## CI/CD & Verification

- PRs require:
  - ✅ Successful multi-framework build/test matrix (net8.0, net9.0, net10.0)
  - ✅ Code coverage report: ≥90%
  - ✅ Component size report for any changed/added packages
  - ✅ Documentation preview builds for any doc changes
  - ✅ Linting/formatting checks passed

---

## Documentation and Catalog Verification

- **Missing docs detection:**  
  Use automated scripts to scan `src/components/` and correlate with `src/apps/Tail.Blazor.Docs/Components/` and `src/apps/Tail.Blazor.Docs/Docs/`.  
  - For any component or feature without a matching docs page, generate an issue or PR to add it.
- **Scope Page Update:**  
  Use a script to periodically update the Scope page with the state of all component and documentation pages, listing every component and every docs page as _existing_ or _missing_.
- **Component & Package Reference Updates:**  
  Whenever you add or modify components or packages, also update all references and relationships in both the documentation and all meta-package/project references.
- **Features Listing:**  
  Main feature checklists (for docs and studio) should also be generated or verified by script, especially for large projects.
- **Stay in sync:**  
  Each addition to the repository (component, doc page, package, guide) must ensure the catalog, navigation, summary indexes, API docs, and all cross-links are complete and up-to-date.
- **No standalone Markdown docs for tracking:**  
  _Do not create or maintain separate Markdown documentation files for catalog or feature tracking—always use and update the Scope pages in the documentation site for these purposes._

---

## Contribution Requirements

1. Every PR _must_ reference an SRS section and append a CHANGELOG entry draft.
2. No placeholder logic, TODO comments, or unfinished code in main branches.
3. No new dependencies, unless justified and approved for core goals.
4. PR description must include:
   - SRS section reference(s)
   - Testing/data to prove compliance (screenshots/coverage/build logs)
   - Size details for each new/changed package
   - Accessibility checklist for new UI components
   - Any API Surface Area changes
5. For meta-packages: only aggregate existing atomic components—never create duplicate/overlapping logic.

---

## Checklist for New Contributions

**Before submitting a PR, ensure ALL the following:**

- [ ] _Component/package builds without warnings on all supported frameworks_
- [ ] _Gzipped `.nupkg` size is within 2-8 KB (or justified as exception)_
- [ ] _≥90% code coverage for new/modified logic (see test report)_
- [ ] _API surface is documented with XML comments_
- [ ] _Component is accessible (WCAG 2.2 AA, ARIA, keyboard support)_
- [ ] _No placeholder/stub/skeleton implementations_
- [ ] _Documentation updated in `/Docs/` and `/Components/` as needed_
- [ ] _CHANGELOG entry draft included in PR description_
- [ ] _All CI checks pass: build, tests, size, docs_
- [ ] _Scope page updated to reflect every component and docs page existence/missing status (use script if possible)_
- [ ] _All component, package, and docs references/relationships updated and correct_
- [ ] _**No new Markdown files created for cataloging, feature, or documentation tracking—use Scope pages only!**_

---

## Final Note

This file is the definitive instruction set for all Tail.Blazor contributors and AI coding agents. No contributions should be merged into production branches without 100% adherence to these requirements.

If you discover a conflict or gap between these instructions and the SRS, immediately document it here and reference in your next PR. 

---

**File generated:** January 4, 2026  
**Maintainer:** Amar-aj  
**Next major review:** After High Priority actions are completed
