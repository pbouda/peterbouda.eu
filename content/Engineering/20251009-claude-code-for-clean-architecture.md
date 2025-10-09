Title: Using Claude Code for clean architecture
Date: 2025-10-09 09:28
Tags: Engineering

I've been using Claude Code to build a Go API with hexagonal architecture, and I'm genuinely impressed. The workflow is smooth: I maintain a CLAUDE.md file with my architecture decisions, add documentation about database models, and then just prompt Claude to implement new endpoints.

Example prompt: _"Add an endpoint to create a new project. You can find information about the database models in plans/database_models.md. For now we only want one more POST endpoint /api/projects that reveives a {"name": "Project name"} JSON. The owner will be the currently logged in user. The training dataset and finetune are empty. The status is ACTIVE"_

Claude Code respects the architecture patterns, follows the established conventions, and produces clean, testable code. Less context-switching between IDE and chat interface.

The full CLAUDE.md template is here if you want to try this approach: [github.com/pbouda/claude-code-prompts/blob/main/CLAUDE_go_api_architecture.md](github.com/pbouda/claude-code-prompts/blob/main/CLAUDE_go_api_architecture.md)

This is what good developer tooling looks like - it understands your codebase and amplifies your architecture decisions rather than fighting them. For me it brought back a lot of joy in developing new software!
