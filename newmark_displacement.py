import pandas as pd
import matplotlib.pyplot as plt

def newmark_displacement(csv_file, yield_acc_g):
    # Load CSV
    df = pd.read_csv(csv_file)
    
    # Ensure proper column names
    df.columns = ['Time', 'Acceleration_g']
    
    # Time step
    dt = df['Time'].diff().fillna(0).mean()
    
    # Compute sliding acceleration
    df['SlidingAcc_g'] = df['Acceleration_g'] - yield_acc_g
    df['SlidingAcc_g'] = df['SlidingAcc_g'].apply(lambda x: x if x > 0 else 0)
    df['SlidingAcc_mps2'] = df['SlidingAcc_g'] * 9.81  # Convert to m/s²

    # Integrate acceleration to velocity & displacement (trapezoidal rule)
    velocity = [0]
    displacement = [0]
    
    for i in range(1, len(df)):
        v = velocity[-1] + 0.5 * (df['SlidingAcc_mps2'][i] + df['SlidingAcc_mps2'][i-1]) * dt
        d = displacement[-1] + 0.5 * (v + velocity[-1]) * dt
        velocity.append(v)
        displacement.append(d)

    df['Velocity_mps'] = velocity
    df['Displacement_m'] = displacement

    # Output total displacement
    final_disp = df['Displacement_m'].iloc[-1]
    print(f"🔧 Final permanent displacement: {final_disp:.4f} meters")

    # Optional plot
    df.plot(x='Time', y='Displacement_m', title='Newmark Displacement')
    plt.ylabel('Displacement (m)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return df

# Example usage:
# df_result = newmark_displacement('acceleration.csv', yield_acc_g=0.06)
