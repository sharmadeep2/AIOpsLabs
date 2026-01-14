# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""Run a specific AIOpsLab problem programmatically."""

import asyncio
from aiopslab.orchestrator import Orchestrator


async def main():
    """Initialize and start the hotel reservation problem."""
    print("Initializing AIOpsLab Orchestrator...")
    orchestrator = Orchestrator()
    orchestrator.agent_name = "human"  # Set agent name
    
    problem_id = "misconfig_app_hotel_res-detection-1"
    print(f"\nStarting problem: {problem_id}")
    print("=" * 80)
    
    try:
        # Initialize the problem
        problem_desc, _, apis = orchestrator.init_problem(problem_id)
        
        print("\n✅ Problem initialized successfully!")
        print("\n" + "=" * 80)
        print("PROBLEM DESCRIPTION:")
        print("=" * 80)
        print(problem_desc)
        print("\n" + "=" * 80)
        print("AVAILABLE APIS:")
        print("=" * 80)
        for api_name, api_desc in apis.items():
            print(f"\n{api_name}:")
            print(api_desc)
        
        print("\n" + "=" * 80)
        print("✅ Hotel Reservation application deployment in progress...")
        print("   This includes:")
        print("   - MongoDB Rate database with initialization scripts")
        print("   - MongoDB Geo database with initialization scripts")
        print("   - All hotel reservation microservices")
        print("   - Prometheus monitoring setup")
        print("=" * 80)
        
        # Keep the script running to monitor deployment
        print("\n⏳ Monitoring deployment status...")
        print("   Check pods with: kubectl get pods -n test-hotel-reservation")
        print("\n   Press Ctrl+C to exit when done inspecting")
        
        # Wait indefinitely
        while True:
            await asyncio.sleep(10)
            
    except KeyboardInterrupt:
        print("\n\n✋ Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
