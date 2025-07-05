# Qwen-Agent - Development Context

## Project Overview
A sophisticated multi-agent framework fork based on QwenLM's official Qwen-Agent repository, featuring custom modifications for enhanced assistant functionality, improved web UI, and specialized configuration optimizations for local and cloud deployment scenarios.

## Git Workflow Strategy
**Strategy**: Fork Strategy

### Workflow Details
- **Main Branch**: `main` - Synced with upstream for compatibility and contributions
- **Private Development Branch**: `private-dev` - Custom modifications and enhancements
- **Upstream Remote**: `upstream` - QwenLM's official Qwen-Agent repository
- **Origin Remote**: `origin` - Personal fork repository
- **Legacy Branch**: `slowbro-qwen` - Previous custom work (preserved as backup)

### Branch Usage Guidelines
- **Sync `main` regularly** with upstream to maintain compatibility
- **All custom development on `private-dev`** branch
- **Feature branches** from `private-dev` for major enhancements
- **Contribution flow**: `main` → upstream (for open source contributions)
- **Custom flow**: `feature/*` → `private-dev` (for private modifications)

## Development Guidelines
- Follow Python best practices and existing Qwen-Agent patterns
- Maintain compatibility with upstream agent APIs where possible
- Update assistant documentation when modifying agent configurations
- Test multi-agent functionality thoroughly before merging changes
- Keep custom modifications well-documented for future upstream integration
- Use descriptive commit messages distinguishing custom vs upstream changes

## Architecture Notes
- **Python multi-agent framework** built on QwenLM's foundation
- **Enhanced assistant configurations** with custom parameter tuning
- **Improved web UI** with usability and functionality enhancements
- **Custom agent implementations** for specialized use cases
- **Multi-model support** including Qwen, OpenAI, and local models
- **MCP integration** for enhanced tool and capability management

## Development Environment
```bash
# Install dependencies
pip install -e .

# Run assistant with custom configurations
python examples/assistant_qwen3.py

# Start enhanced web UI
python qwen_agent/gui/web_ui.py

# Run multi-agent demos
python examples/group_chat_demo.py
python examples/multi_agent_router.py

# Test custom modifications
python -m pytest tests/

# Start server with custom settings
python run_server.py
```

## Key Files and Directories
- `examples/assistant_qwen3.py` - Enhanced assistant with custom configurations
- `qwen_agent/gui/web_ui.py` - Improved web interface with custom modifications
- `qwen_agent/agents/` - Core agent implementations and enhancements
- `qwen_agent/tools/` - Tool integrations including MCP manager
- `MIGRATION.md` - Fork strategy documentation and workflow guidance
- `tests/` - Comprehensive test suite for custom modifications

## Current Development Focus
Fork Strategy with active agent enhancements:
- **Assistant optimization**: Enhanced configuration and performance tuning
- **Web UI improvements**: Better usability and functionality
- **Multi-agent coordination**: Advanced agent interaction patterns
- **Tool integration**: Enhanced MCP and custom tool support
- **Upstream compatibility**: Maintaining sync with QwenLM developments

## Dependencies and Integration
- **QwenLM Qwen-Agent**: Upstream base framework requiring regular sync
- **Multiple LLM backends**: Qwen models, OpenAI, Anthropic, local models
- **Web frameworks**: Gradio, Flask for enhanced UI components
- **MCP protocol**: Model Context Protocol for tool and capability management
- **Python ecosystem**: Core ML and agent libraries
- **Custom enhancements**: Specialized configurations and optimizations

## Notes and Context
- **Production-ready fork** with enhanced capabilities beyond upstream
- **Custom agent configurations** optimized for specific use cases
- **Enhanced web interface** with improved user experience
- **Upstream sync strategy** for ongoing compatibility and contributions
- **Multi-model flexibility** supporting various LLM backends
- **Well-documented customizations** for potential upstream contribution
- **Active development** balancing custom features with upstream compatibility