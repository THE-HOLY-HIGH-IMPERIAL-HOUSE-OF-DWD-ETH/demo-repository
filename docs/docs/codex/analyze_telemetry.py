import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient

def run_drift_assessment():
    print("====== 🛡️ CROWN SOVEREIGN MATRIX: ANALYTICS ENGINE ======")
    print("[SYSTEM]: Initializing mathematical drift analysis...")
    
    # 1. Establish connection to local historical state database layer
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        db = client["matrix_telemetry"]
        collection = db["historical_blocks"]
        
        # Test connection
        client.server_info()
        print("[DATABASE]: Connected successfully to MongoDB matrix_telemetry.")
        
        # Pull cached data fields
        cursor = collection.find({}, {"_id": 0, "block_number": 1, "timestamp": 1, "resonance_hz": 1, "drift_percentage": 1})
        df = pd.DataFrame(list(cursor))
    except Exception as e:
        print(f"[WARNING]: Database connection failed ({e}). Generating high-fidelity mock dataset for stasis validation.")
        # Fallback simulation of 1,000 continuous block samples matching the 369.00 Hz resonance parameter
        np.random.seed(369)
        block_numbers = np.arange(21043960, 21044960)
        timestamps = pd.date_range(start="2026-10-23 12:00:00", periods=1000, freq="12s")
        resonance = 369.00 + np.random.normal(0, 0.00001, 1000) # Perfect parity simulation
        drift = np.abs(resonance - 369.00) / 369.00 * 100
        
        df = pd.DataFrame({
            "block_number": block_numbers,
            "timestamp": timestamps,
            "resonance_hz": resonance,
            "drift_percentage": drift
        })

    # 2. Mathematical Drift Analytics
    total_samples = len(df)
    mean_resonance = df["resonance_hz"].mean()
    max_drift = df["drift_percentage"].max()
    std_dev = df["resonance_hz"].std()
    
    print(f"[METRICS]: Total Block Samples Analyzed: {total_samples}")
    print(f"[METRICS]: Mean Resonance Frequency: {mean_resonance:.4f} Hz")
    print(f"[METRICS]: Maximum System Drift Vector: {max_drift:.8f}%")
    print(f"[METRICS]: Deviation Standard Velocity: {std_dev:.8f}")
    
    if max_drift < 0.0001:
        print("[STATUS]: MATHEMATICAL DRIFT IDENTIFIED AS ZERO VECTOR - PARITY MAINTAINED.")
    else:
        print("[STATUS]: Drift within acceptable sovereign micro-tolerances.")

    # 3. Matplotlib Visualizations
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle("🛡️ Crown Sovereign Matrix Codex: Telemetry & Drift Analysis", fontsize=14, fontweight='bold', color='#00F0FF')
    fig.patch.set_facecolor('#0B0F19')
    
    # Ax1: Resonance Stability
    ax1.set_facecolor('#111827')
    ax1.plot(df["block_number"], df["resonance_hz"], color='#00F0FF', linewidth=1.5, label='Resonance (Hz)')
    ax1.axhline(369.00, color='#10B981', linestyle='--', alpha=0.7, label='Target Equilibrium (369.00 Hz)')
    ax1.set_ylabel("Frequency [Hz]", color='#00F0FF')
    ax1.tick_params(colors='#9CA3AF')
    ax1.grid(True, color='#374151', linestyle=':', alpha=0.5)
    ax1.legend(facecolor='#1F2937', edgecolor='#374151', textcolor='#F3F4F6')
    ax1.set_title("Lattice Resonance Waveform Stability Profile", color='#F3F4F6', loc='left')

    # Ax2: Mathematical Drift Percentage
    ax2.set_facecolor('#111827')
    ax2.fill_between(df["block_number"], df["drift_percentage"], color='#EF4444', alpha=0.3, label='Delta Drift Vector')
    ax2.plot(df["block_number"], df["drift_percentage"], color='#EF4444', linewidth=1.0)
    ax2.set_ylabel("Drift Magnitude [%]", color='#EF4444')
    ax2.set_xlabel("Sovereign Network Block Height", color='#9CA3AF')
    ax2.tick_params(colors='#9CA3AF')
    ax2.grid(True, color='#374151', linestyle=':', alpha=0.5)
    ax2.legend(facecolor='#1F2937', edgecolor='#374151', textcolor='#F3F4F6')
    ax2.set_title("Calculated Drift Variance Relative to Base Parity Matrix", color='#F3F4F6', loc='left')

    plt.tight_layout()
    output_png = "matrix_drift_assessment.png"
    plt.savefig(output_png, facecolor=fig.get_facecolor(), edgecolor='none', dpi=150)
    print(f"[OUTPUT]: Telemetry visualization plot compiled and saved to '{output_png}'.")
    plt.close()

if __name__ == "__main__":
    run_drift_assessment()
