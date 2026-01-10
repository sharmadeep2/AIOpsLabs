# AIOpsLabs - Local Deployment

This repository contains a local deployment of Microsoft's AIOpsLab framework for developing and evaluating AIOps agents.

## 🚀 How to Use AIOpsLab

### Prerequisites

Make sure you have the following installed:
- Python >= 3.11 (Python 3.12 recommended for best compatibility)
- [Docker](https://docs.docker.com/get-started/get-docker/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)

### Quick Start

1. **Navigate to the AIOpsLab directory**:
   ```bash
   cd AIOpsLab
   ```

2. **Activate the Python environment**:
   ```bash
   # Activate the virtual environment
   .\aiopslab-env\Scripts\Activate.ps1   # Windows
   # OR use the configured Python environment path
   ```

3. **Configure AIOpsLab**:
   ```bash
   cd AIOpsLab/aiopslab
   cp config.yml.example config.yml
   # Edit config.yml to set k8s_host: kind and your username
   ```

4. **Verify the kind cluster is running**:
4. **Verify the kind cluster is running**:
   ```bash
   kubectl cluster-info --context kind-kind
   kubectl get nodes
   ```

5. **Run the AIOpsLab CLI**:
   ```bash
   python cli.py
   ```

### Available Commands

Once in the AIOpsLab CLI:

- **List available problems**:
  ```bash
  # Run in Python to see available problems
  from aiopslab.orchestrator import Orchestrator
  orch = Orchestrator()
  print(orch.probs.get_problem_ids())
  ```

- **Start a problem**:
  ```bash
  aiopslab> start misconfig_app_hotel_res-detection-1
  ```

- **Submit a solution**:
  ```bash
  aiopslab> submit("Your solution here")
  ```

- **Exit the CLI**:
  ```bash
  aiopslab> exit
  ```

### Example Problems Available

The system includes 82+ problems covering various scenarios:
- **Kubernetes Issues**: `k8s_target_port-misconfig-detection-1`
- **Database Problems**: `auth_miss_mongodb-detection-1`
- **Application Issues**: `misconfig_app_hotel_res-detection-1`
- **Scaling Problems**: `scale_pod_zero_social_net-detection-1`
- **Network Issues**: `network_loss_hotel_res-detection-1`
- **Container Failures**: `container_kill-detection`
- **Service Failures**: `astronomy_shop_ad_service_failure-detection-1`

### Using AI Agents

To use AI agents like GPT-4:

1. **Create environment file**:
   ```bash
   cp .env.template .env
   ```

2. **Add your API keys to .env**:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   # Optional:
   QWEN_API_KEY=your_qwen_api_key_here
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   USE_WANDB=false
   ```

3. **Run GPT-4 baseline agent**:
   ```bash
   python clients/gpt.py
   ```

### Monitoring Your Cluster

- **View cluster information**:
  ```bash
  kubectl cluster-info
  kubectl get nodes
  kubectl get pods --all-namespaces
  ```

- **Monitor with k9s** (if installed):
  ```bash
  k9s
  ```

### Configuration

The system is configured with:
- **k8s_host**: `kind` (for local kind cluster)
- **Data directory**: `data/`
- **SSH key**: `~/.ssh/id_rsa`
- **Qualitative evaluation**: disabled by default

Configuration file: `AIOpsLab/aiopslab/config.yml`

### Troubleshooting

If you encounter issues:

1. **Check cluster status**:
   ```bash
   kind get clusters
   kubectl get nodes
   ```

2. **Restart kind cluster if needed**:
   ```bash
   kind delete cluster
   kind create cluster --config AIOpsLab/kind/kind-config-x86.yaml
   ```

3. **Verify Python dependencies**:
   ```bash
   pip list | grep -E "(openai|kubernetes|pandas)"
   ```

## 📁 Project Structure

```
AIOpsLabs/
├── AIOpsLab/                 # Main AIOpsLab framework
│   ├── aiopslab/            # Core framework code
│   │   ├── orchestrator/    # Problem orchestration
│   │   ├── service/         # Application services
│   │   └── config.yml       # Configuration file
│   ├── clients/             # AI agent clients
│   ├── kind/               # Kubernetes kind configuration
│   ├── cli.py              # Command-line interface
│   └── .env.template       # Environment template
└── README.md               # This file
```

## 🎯 Getting Started with Your First Problem

1. Start the CLI: `python cli.py`
2. Try a simple detection problem: `start misconfig_app_hotel_res-detection-1`
3. Wait for the setup to complete
4. Interact with the problem environment
5. Submit your solution: `submit("Your analysis or fix here")`

## 📚 Additional Resources

- [Original AIOpsLab Repository](https://github.com/microsoft/AIOpsLab)
- [AIOpsLab Documentation](https://github.com/microsoft/AIOpsLab/blob/main/README.md)
- [Kind Documentation](https://kind.sigs.k8s.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

---

**Note**: This is a local deployment setup for development and testing purposes. Some advanced features requiring specific cloud resources may not be available in this local setup.