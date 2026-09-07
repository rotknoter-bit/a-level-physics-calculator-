135
import math



c     = 3.00e8        # speed of light in vacuo (m s^-1)
mu0   = 4 * math.pi * 1e-7   # permeability of free space (H m^-1)
e0    = 8.85e-12      # permittivity of free space (F m^-1)
e     = 1.60e-19      # magnitude of the charge of electron (C)
h     = 6.63e-34      # the Planck constant (J s)
G     = 6.67e-11      # gravitational constant (N m^2 kg^-2)
NA    = 6.02e23       # the Avogadro constant (mol^-1)
R_gas = 8.31          # molar gas constant (J K^-1 mol^-1)
k_B   = 1.38e-23      # the Boltzmann constant (J K^-1)
sigma = 5.67e-8       # the Stefan constant (W m^-2 K^-4)
me    = 9.11e-31      # electron rest mass (kg)
mp    = 1.673e-27     # proton rest mass (kg)
mn    = 1.675e-27     # neutron rest mass (kg)
g     = 9.81          # gravitational field strength / acceleration due to gravity

equations = {
    
    "F=ma": "Force = mass * acceleration",
    "V=U+AT": "Final velocity = Initial velocity + Acceleration * Time",

    
    "moment=Fd": "Moment = Force * perpendicular distance",
    "s=(u+v)/2*t": "Displacement = average velocity * time",
    "v^2=u^2+2as": "Final velocity squared = u^2 + 2*acceleration*displacement",
    "s=ut+0.5at^2": "Displacement = u*t + 0.5*acceleration*time^2",
    "W=Fscostheta": "Work done = Force * distance * cos(angle)",
    "Ek=0.5mv^2": "Kinetic energy = 0.5 * mass * velocity^2",
    "dEp=mgdh": "Change in gravitational PE = mass * g * change in height",
    "P=W/t": "Power = work done / time",
    "P=Fv": "Power = Force * velocity",
    "efficiency": "Efficiency = useful output power / input power",

    
    "rho=m/V": "Density = mass / volume",
    "F=kdL": "Hooke's law: Force = spring constant * extension",
    "E=stress/strain": "Young modulus = tensile stress / tensile strain",
    "stress=F/A": "Tensile stress = Force / cross-sectional area",
    "strain=dL/L": "Tensile strain = extension / original length",
    "E=0.5FdL": "Energy stored in a stretched material = 0.5 * Force * extension",

    
    "E=hf": "Photon energy = Planck constant * frequency",
    "E=hc/lambda": "Photon energy = h*c / wavelength",
    "hf=phi+Ek": "Photoelectric effect: h*f = work function + max kinetic energy",
    "hf=E1-E2": "Energy levels: h*f = E1 - E2",
    "lambda=h/mv": "de Broglie wavelength = h / (mass * velocity)",
    "v=flambda": "Wave speed = frequency * wavelength",
    "f=1/T": "Frequency = 1 / period",
    "f=(1/2l)sqrt(T/mu)": "First harmonic of a string",
    "w=lambdaD/s": "Fringe spacing = wavelength * slit-screen distance / slit separation",
    "dsintheta=nlambda": "Diffraction grating: d*sin(theta) = n*wavelength",
    "n=c/cs": "Refractive index = c / speed in substance",
    "n1sintheta1=n2sintheta2": "Snell's law of refraction",
    "sinthetac=n2/n1": "Critical angle: sin(theta_c) = n2 / n1",

    
    "I=Q/t": "Current = charge / time",
    "V=W/Q": "Potential difference = work done / charge",
    "R=V/I": "Resistance = pd / current",
    "rho=RA/L": "Resistivity = resistance * area / length",
    "Rseries": "Resistors in series: RT = R1 + R2 + R3",
    "Rparallel": "Resistors in parallel: 1/RT = 1/R1 + 1/R2 + 1/R3",
    "P=VI": "Power = pd * current",
    "P=I^2R": "Power = current^2 * resistance",
    "P=V^2/R": "Power = pd^2 / resistance",
    "emf=E/Q": "emf = energy / charge",
    "emf=I(R+r)": "emf = current * (resistance + internal resistance)",


    "omega=v/r": "Angular speed = linear speed / radius",
    "omega=2pif": "Angular speed = 2*pi*frequency",
    "a=v^2/r": "Centripetal acceleration = v^2 / r",
    "a=omega^2r": "Centripetal acceleration = omega^2 * r",
    "F=mv^2/r": "Centripetal force = m*v^2 / r",
    "F=momega^2r": "Centripetal force = m*omega^2*r",


    "a=-omega^2x": "SHM acceleration = -omega^2 * displacement",
    "x=Acos(omegat)": "SHM displacement = amplitude * cos(omega*t)",
    "v=omegasqrt(A^2-x^2)": "SHM speed = omega * sqrt(A^2 - x^2)",
    "vmax=omegaA": "SHM maximum speed = omega * amplitude",
    "amax=omega^2A": "SHM maximum acceleration = omega^2 * amplitude",
    "T=2pisqrt(m/k)": "Period of a mass-spring system",
    "T=2pisqrt(l/g)": "Period of a simple pendulum",

    
    "Q=mcdtheta": "Energy to change temperature = mass * specific heat * temp change",
    "Q=ml": "Energy to change state = mass * specific latent heat",
    "pV=nRT": "Ideal gas law (moles)",
    "pV=NkT": "Ideal gas law (number of molecules)",
    "pV=(1/3)Nmcrms^2": "Kinetic theory model",
    "0.5mcrms^2=1.5kT": "Mean kinetic energy of a gas molecule",

    
    "F=Gm1m2/r^2": "Newton's law of gravitation",
    "g=F/m": "Gravitational field strength = force / mass",
    "g=GM/r^2": "Radial gravitational field strength",
    "dW=mdV": "Work done = mass * change in gravitational potential",
    "Vgrav=-GM/r": "Gravitational potential = -G*M / r",

    
    "F=Q1Q2/4pie0r^2": "Coulomb's law: force between two point charges",
    "F=EQ": "Force on a charge = field strength * charge",
    "E=V/d": "Field strength for a uniform field = pd / separation",
    "dW=QdV": "Work done = charge * change in potential",
    "E=Q/4pie0r^2": "Radial electric field strength",
    "Velec=Q/4pie0r": "Electric potential",
    "C=Q/V": "Capacitance = charge / pd",
    "C=Ae0er/d": "Parallel-plate capacitance",
    "E=0.5QV": "Energy stored in a capacitor = 0.5*Q*V",
    "E=0.5CV^2": "Energy stored in a capacitor = 0.5*C*V^2",
    "E=0.5Q^2/C": "Energy stored in a capacitor = 0.5*Q^2 / C",
    "Q=Q0(1-e^-t/RC)": "Capacitor charging",
    "Q=Q0e^-t/RC": "Capacitor charge decay",

    
    "F=BIl": "Force on a current-carrying wire",
    "F=BQv": "Force on a moving charge",
    "flux=BA": "Magnetic flux = flux density * area",
    "fluxlinkage=BANcostheta": "Magnetic flux linkage",
    "emf=NdPhi/dt": "Magnitude of induced emf",
    "emf=BANomegasin": "emf induced in a rotating coil (peak when sin = 1)",
    "Irms=I0/sqrt2": "RMS current",
    "Vrms=V0/sqrt2": "RMS voltage",
    "Ns/Np=Vs/Vp": "Transformer equation",
    "transformereff": "Transformer efficiency = Is*Vs / (Ip*Vp)",

    
    "I=k/x^2": "Inverse square law for gamma radiation",
    "N=N0e^-lambdat": "Radioactive decay",
    "A=lambdaN": "Activity = decay constant * number of nuclei",
    "halflife": "Half-life = ln(2) / decay constant",
    "R=R0A^(1/3)": "Nuclear radius",
    "E=mc^2": "Energy-mass equation",

   
    "M=f0/fe": "Telescope angular magnification = f_objective / f_eyepiece",
    "theta=lambda/D": "Rayleigh criterion",
    "m-M=5log(d/10)": "Magnitude equation (d in parsecs)",
    "lambdamaxT=2.9e-3": "Wien's law",
    "P=sigmaAT^4": "Stefan's law",
    "Rs=2GM/c^2": "Schwarzschild radius",
    "z=v/c": "Red shift",
    "v=Hd": "Hubble's law (H in km/s per Mpc, d in Mpc)",

    
    "P=1/f": "Lens power = 1 / focal length",
    "m=v/u": "Magnification = image distance / object distance",
    "1/f=1/u+1/v": "Thin lens equation",
    "level=10log(I/I0)": "Intensity level in dB",
    "I=I0e^-mux": "Attenuation of radiation",
    "mum=mu/rho": "Mass attenuation coefficient",
    "Z=rhoc": "Acoustic impedance",
    "1/TE=1/TB+1/TP": "Effective half-life",

    
    "I=mr^2": "Moment of inertia of a point mass",
    "Ek=0.5Iomega^2": "Angular kinetic energy",
    "omega2=omega1+alphat": "Angular motion: final = initial + alpha*t",
    "omega2^2=omega1^2+2alphatheta": "Angular motion: omega2^2 = omega1^2 + 2*alpha*theta",
    "theta=omega1t+0.5alphat^2": "Angular motion: theta = omega1*t + 0.5*alpha*t^2",
    "T=Ialpha": "Torque = moment of inertia * angular acceleration",
    "T=Fr": "Torque = Force * radius",
    "L=Iomega": "Angular momentum = I * omega",
    "W=Ttheta": "Work done by a torque = torque * angle",
    "P=Tomega": "Power = torque * angular speed",
    "Q=dU+W": "First law of thermodynamics",
    "W=pdV": "Work done by a gas = pressure * change in volume",
    "engineeff": "Heat engine efficiency = (QH - QC) / QH",
    "maxeff": "Maximum theoretical efficiency = (TH - TC) / TH",
    "COPref": "Refrigerator COP = QC / (QH - QC)",
    "COPhp": "Heat pump COP = QH / (QH - QC)",

   
    "F=eV/d": "Force on an electron between charged plates",
    "F=Bev": "Force on an electron in a magnetic field",
    "r=mv/Be": "Radius of an electron's path in a magnetic field",
    "0.5mv^2=eV": "Kinetic energy gained by an accelerated electron",
    "QV/d=mg": "Millikan's experiment (balanced oil drop)",
    "F=6pietarv": "Stokes' law (viscous drag on a sphere)",
    "lambda=h/sqrt(2meV)": "Electron de Broglie wavelength after acceleration",
    "t=t0/sqrt(1-v^2/c^2)": "Time dilation",
    "l=l0sqrt(1-v^2/c^2)": "Length contraction",

    
    "f0=1/2pisqrt(LC)": "Resonant frequency",
    "Q=f0/fB": "Q-factor",
}


keys = list(equations)
print("Available equations:\n")
for i, key in enumerate(keys, start=1):
    print(f"  {i}. {key}  ->  {equations[key]}")

number = input("\npick an equation by number: ").strip()

if not number.isdigit() or not (1 <= int(number) <= len(keys)):
    print("Invalid choice")
else:
    choice = keys[int(number) - 1]
    selected = equations[choice]
    print(f"\nyou selected: {choice}  ({selected})\n")



    if choice == "F=ma":
        variable = input("what do you want to solve for? (F, m, a): ").strip()
        if variable == "F":
            m = float(input("Enter mass (m): "))
            a = float(input("Enter acceleration (a): "))
            print(f"Force (F) = {m * a}")
        elif variable == "m":
            F = float(input("Enter force (F): "))
            a = float(input("Enter acceleration (a): "))
            print(f"Mass (m) = {F / a}")
        elif variable == "a":
            F = float(input("Enter force (F): "))
            m = float(input("Enter mass (m): "))
            print(f"Acceleration (a) = {F / m}")
        else:
            print("Invalid variable choice")

    elif choice == "V=U+AT":
        variable = input("what do you want to solve for? (V, U, A, T): ").strip()
        if variable == "V":
            U = float(input("Enter initial velocity (U): "))
            A = float(input("Enter acceleration (A): "))
            T = float(input("Enter time (T): "))
            print(f"Final velocity (V) = {U + A * T}")
        elif variable == "U":
            V = float(input("Enter final velocity (V): "))
            A = float(input("Enter acceleration (A): "))
            T = float(input("Enter time (T): "))
            print(f"Initial velocity (U) = {V - A * T}")
        elif variable == "A":
            V = float(input("Enter final velocity (V): "))
            U = float(input("Enter initial velocity (U): "))
            T = float(input("Enter time (T): "))
            print(f"Acceleration (A) = {(V - U) / T}")
        elif variable == "T":
            V = float(input("Enter final velocity (V): "))
            U = float(input("Enter initial velocity (U): "))
            A = float(input("Enter acceleration (A): "))
            print(f"Time (T) = {(V - U) / A}")
        else:
            print("Invalid variable choice")

    elif choice == "moment=Fd":
        variable = input("solve for? (moment, F, d): ").strip()
        if variable == "moment":
            F = float(input("Enter force (F): "))
            d = float(input("Enter perpendicular distance (d): "))
            print(f"Moment = {F * d}")
        elif variable == "F":
            moment = float(input("Enter moment: "))
            d = float(input("Enter perpendicular distance (d): "))
            print(f"Force (F) = {moment / d}")
        elif variable == "d":
            moment = float(input("Enter moment: "))
            F = float(input("Enter force (F): "))
            print(f"Distance (d) = {moment / F}")
        else:
            print("Invalid variable choice")

    elif choice == "s=(u+v)/2*t":
        variable = input("solve for? (s, u, v, t): ").strip()
        if variable == "s":
            u = float(input("Enter initial velocity (u): "))
            v = float(input("Enter final velocity (v): "))
            t = float(input("Enter time (t): "))
            print(f"Displacement (s) = {(u + v) / 2 * t}")
        elif variable == "u":
            s = float(input("Enter displacement (s): "))
            v = float(input("Enter final velocity (v): "))
            t = float(input("Enter time (t): "))
            print(f"Initial velocity (u) = {2 * s / t - v}")
        elif variable == "v":
            s = float(input("Enter displacement (s): "))
            u = float(input("Enter initial velocity (u): "))
            t = float(input("Enter time (t): "))
            print(f"Final velocity (v) = {2 * s / t - u}")
        elif variable == "t":
            s = float(input("Enter displacement (s): "))
            u = float(input("Enter initial velocity (u): "))
            v = float(input("Enter final velocity (v): "))
            print(f"Time (t) = {2 * s / (u + v)}")
        else:
            print("Invalid variable choice")

    elif choice == "v^2=u^2+2as":
        variable = input("solve for? (v, u, a, s): ").strip()
        if variable == "v":
            u = float(input("Enter initial velocity (u): "))
            a = float(input("Enter acceleration (a): "))
            s = float(input("Enter displacement (s): "))
            print(f"Final velocity (v) = {math.sqrt(u**2 + 2 * a * s)}")
        elif variable == "u":
            v = float(input("Enter final velocity (v): "))
            a = float(input("Enter acceleration (a): "))
            s = float(input("Enter displacement (s): "))
            print(f"Initial velocity (u) = {math.sqrt(v**2 - 2 * a * s)}")
        elif variable == "a":
            v = float(input("Enter final velocity (v): "))
            u = float(input("Enter initial velocity (u): "))
            s = float(input("Enter displacement (s): "))
            print(f"Acceleration (a) = {(v**2 - u**2) / (2 * s)}")
        elif variable == "s":
            v = float(input("Enter final velocity (v): "))
            u = float(input("Enter initial velocity (u): "))
            a = float(input("Enter acceleration (a): "))
            print(f"Displacement (s) = {(v**2 - u**2) / (2 * a)}")
        else:
            print("Invalid variable choice")

    elif choice == "s=ut+0.5at^2":
        variable = input("solve for? (s, u, a, t): ").strip()
        if variable == "s":
            u = float(input("Enter initial velocity (u): "))
            t = float(input("Enter time (t): "))
            a = float(input("Enter acceleration (a): "))
            print(f"Displacement (s) = {u * t + 0.5 * a * t**2}")
        elif variable == "u":
            s = float(input("Enter displacement (s): "))
            t = float(input("Enter time (t): "))
            a = float(input("Enter acceleration (a): "))
            print(f"Initial velocity (u) = {(s - 0.5 * a * t**2) / t}")
        elif variable == "a":
            s = float(input("Enter displacement (s): "))
            u = float(input("Enter initial velocity (u): "))
            t = float(input("Enter time (t): "))
            print(f"Acceleration (a) = {2 * (s - u * t) / t**2}")
        elif variable == "t":
            s = float(input("Enter displacement (s): "))
            u = float(input("Enter initial velocity (u): "))
            a = float(input("Enter acceleration (a): "))
            if a == 0:
                print(f"Time (t) = {s / u}")
            else:
                print(f"Time (t) = {(-u + math.sqrt(u**2 + 2 * a * s)) / a}")
        else:
            print("Invalid variable choice")

    elif choice == "W=Fscostheta":
        variable = input("solve for? (W, F, s, theta): ").strip()
        if variable == "W":
            F = float(input("Enter force (F): "))
            s = float(input("Enter distance (s): "))
            theta = float(input("Enter angle in degrees (theta): "))
            print(f"Work done (W) = {F * s * math.cos(math.radians(theta))}")
        elif variable == "F":
            W = float(input("Enter work done (W): "))
            s = float(input("Enter distance (s): "))
            theta = float(input("Enter angle in degrees (theta): "))
            print(f"Force (F) = {W / (s * math.cos(math.radians(theta)))}")
        elif variable == "s":
            W = float(input("Enter work done (W): "))
            F = float(input("Enter force (F): "))
            theta = float(input("Enter angle in degrees (theta): "))
            print(f"Distance (s) = {W / (F * math.cos(math.radians(theta)))}")
        elif variable == "theta":
            W = float(input("Enter work done (W): "))
            F = float(input("Enter force (F): "))
            s = float(input("Enter distance (s): "))
            print(f"Angle (theta) = {math.degrees(math.acos(W / (F * s)))} degrees")
        else:
            print("Invalid variable choice")

    elif choice == "Ek=0.5mv^2":
        variable = input("solve for? (Ek, m, v): ").strip()
        if variable == "Ek":
            m = float(input("Enter mass (m): "))
            v = float(input("Enter velocity (v): "))
            print(f"Kinetic energy (Ek) = {0.5 * m * v**2}")
        elif variable == "m":
            Ek = float(input("Enter kinetic energy (Ek): "))
            v = float(input("Enter velocity (v): "))
            print(f"Mass (m) = {2 * Ek / v**2}")
        elif variable == "v":
            Ek = float(input("Enter kinetic energy (Ek): "))
            m = float(input("Enter mass (m): "))
            print(f"Velocity (v) = {math.sqrt(2 * Ek / m)}")
        else:
            print("Invalid variable choice")

    elif choice == "dEp=mgdh":
        variable = input("solve for? (dEp, m, dh): ").strip()
        if variable == "dEp":
            m = float(input("Enter mass (m): "))
            dh = float(input("Enter change in height (dh): "))
            print(f"Change in PE (dEp) = {m * g * dh}")
        elif variable == "m":
            dEp = float(input("Enter change in PE (dEp): "))
            dh = float(input("Enter change in height (dh): "))
            print(f"Mass (m) = {dEp / (g * dh)}")
        elif variable == "dh":
            dEp = float(input("Enter change in PE (dEp): "))
            m = float(input("Enter mass (m): "))
            print(f"Change in height (dh) = {dEp / (m * g)}")
        else:
            print("Invalid variable choice")

    elif choice == "P=W/t":
        variable = input("solve for? (P, W, t): ").strip()
        if variable == "P":
            W = float(input("Enter work done (W): "))
            t = float(input("Enter time (t): "))
            print(f"Power (P) = {W / t}")
        elif variable == "W":
            P = float(input("Enter power (P): "))
            t = float(input("Enter time (t): "))
            print(f"Work done (W) = {P * t}")
        elif variable == "t":
            P = float(input("Enter power (P): "))
            W = float(input("Enter work done (W): "))
            print(f"Time (t) = {W / P}")
        else:
            print("Invalid variable choice")

    elif choice == "P=Fv":
        variable = input("solve for? (P, F, v): ").strip()
        if variable == "P":
            F = float(input("Enter force (F): "))
            v = float(input("Enter velocity (v): "))
            print(f"Power (P) = {F * v}")
        elif variable == "F":
            P = float(input("Enter power (P): "))
            v = float(input("Enter velocity (v): "))
            print(f"Force (F) = {P / v}")
        elif variable == "v":
            P = float(input("Enter power (P): "))
            F = float(input("Enter force (F): "))
            print(f"Velocity (v) = {P / F}")
        else:
            print("Invalid variable choice")

    elif choice == "efficiency":
        variable = input("solve for? (efficiency, output, input): ").strip()
        if variable == "efficiency":
            out = float(input("Enter useful output power: "))
            inp = float(input("Enter input power: "))
            print(f"Efficiency = {out / inp}  ({out / inp * 100} %)")
        elif variable == "output":
            eff = float(input("Enter efficiency (as a decimal): "))
            inp = float(input("Enter input power: "))
            print(f"Useful output power = {eff * inp}")
        elif variable == "input":
            eff = float(input("Enter efficiency (as a decimal): "))
            out = float(input("Enter useful output power: "))
            print(f"Input power = {out / eff}")
        else:
            print("Invalid variable choice")

   
    elif choice == "rho=m/V":
        variable = input("solve for? (rho, m, V): ").strip()
        if variable == "rho":
            m = float(input("Enter mass (m): "))
            V = float(input("Enter volume (V): "))
            print(f"Density (rho) = {m / V}")
        elif variable == "m":
            rho = float(input("Enter density (rho): "))
            V = float(input("Enter volume (V): "))
            print(f"Mass (m) = {rho * V}")
        elif variable == "V":
            rho = float(input("Enter density (rho): "))
            m = float(input("Enter mass (m): "))
            print(f"Volume (V) = {m / rho}")
        else:
            print("Invalid variable choice")

    elif choice == "F=kdL":
        variable = input("solve for? (F, k, dL): ").strip()
        if variable == "F":
            k = float(input("Enter spring constant (k): "))
            dL = float(input("Enter extension (dL): "))
            print(f"Force (F) = {k * dL}")
        elif variable == "k":
            F = float(input("Enter force (F): "))
            dL = float(input("Enter extension (dL): "))
            print(f"Spring constant (k) = {F / dL}")
        elif variable == "dL":
            F = float(input("Enter force (F): "))
            k = float(input("Enter spring constant (k): "))
            print(f"Extension (dL) = {F / k}")
        else:
            print("Invalid variable choice")

    elif choice == "E=stress/strain":
        variable = input("solve for? (E, stress, strain): ").strip()
        if variable == "E":
            stress = float(input("Enter tensile stress: "))
            strain = float(input("Enter tensile strain: "))
            print(f"Young modulus (E) = {stress / strain}")
        elif variable == "stress":
            E = float(input("Enter Young modulus (E): "))
            strain = float(input("Enter tensile strain: "))
            print(f"Tensile stress = {E * strain}")
        elif variable == "strain":
            E = float(input("Enter Young modulus (E): "))
            stress = float(input("Enter tensile stress: "))
            print(f"Tensile strain = {stress / E}")
        else:
            print("Invalid variable choice")

    elif choice == "stress=F/A":
        variable = input("solve for? (stress, F, A): ").strip()
        if variable == "stress":
            F = float(input("Enter force (F): "))
            A = float(input("Enter cross-sectional area (A): "))
            print(f"Tensile stress = {F / A}")
        elif variable == "F":
            stress = float(input("Enter tensile stress: "))
            A = float(input("Enter cross-sectional area (A): "))
            print(f"Force (F) = {stress * A}")
        elif variable == "A":
            stress = float(input("Enter tensile stress: "))
            F = float(input("Enter force (F): "))
            print(f"Area (A) = {F / stress}")
        else:
            print("Invalid variable choice")

    elif choice == "strain=dL/L":
        variable = input("solve for? (strain, dL, L): ").strip()
        if variable == "strain":
            dL = float(input("Enter extension (dL): "))
            L = float(input("Enter original length (L): "))
            print(f"Tensile strain = {dL / L}")
        elif variable == "dL":
            strain = float(input("Enter tensile strain: "))
            L = float(input("Enter original length (L): "))
            print(f"Extension (dL) = {strain * L}")
        elif variable == "L":
            strain = float(input("Enter tensile strain: "))
            dL = float(input("Enter extension (dL): "))
            print(f"Original length (L) = {dL / strain}")
        else:
            print("Invalid variable choice")

    elif choice == "E=0.5FdL":
        variable = input("solve for? (E, F, dL): ").strip()
        if variable == "E":
            F = float(input("Enter force (F): "))
            dL = float(input("Enter extension (dL): "))
            print(f"Energy stored (E) = {0.5 * F * dL}")
        elif variable == "F":
            E = float(input("Enter energy stored (E): "))
            dL = float(input("Enter extension (dL): "))
            print(f"Force (F) = {2 * E / dL}")
        elif variable == "dL":
            E = float(input("Enter energy stored (E): "))
            F = float(input("Enter force (F): "))
            print(f"Extension (dL) = {2 * E / F}")
        else:
            print("Invalid variable choice")

    # =====================================================================
    # WAVES & PHOTONS
    # =====================================================================
    elif choice == "E=hf":
        variable = input("solve for? (E, f): ").strip()
        if variable == "E":
            f = float(input("Enter frequency (f): "))
            print(f"Photon energy (E) = {h * f} J")
        elif variable == "f":
            E = float(input("Enter photon energy (E): "))
            print(f"Frequency (f) = {E / h} Hz")
        else:
            print("Invalid variable choice")

    elif choice == "E=hc/lambda":
        variable = input("solve for? (E, lambda): ").strip()
        if variable == "E":
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Photon energy (E) = {h * c / lam} J")
        elif variable == "lambda":
            E = float(input("Enter photon energy (E): "))
            print(f"Wavelength (lambda) = {h * c / E} m")
        else:
            print("Invalid variable choice")

    elif choice == "hf=phi+Ek":
        variable = input("solve for? (f, phi, Ek): ").strip()
        if variable == "f":
            phi = float(input("Enter work function (phi): "))
            Ek = float(input("Enter max kinetic energy (Ek): "))
            print(f"Frequency (f) = {(phi + Ek) / h} Hz")
        elif variable == "phi":
            f = float(input("Enter frequency (f): "))
            Ek = float(input("Enter max kinetic energy (Ek): "))
            print(f"Work function (phi) = {h * f - Ek} J")
        elif variable == "Ek":
            f = float(input("Enter frequency (f): "))
            phi = float(input("Enter work function (phi): "))
            print(f"Max kinetic energy (Ek) = {h * f - phi} J")
        else:
            print("Invalid variable choice")

    elif choice == "hf=E1-E2":
        variable = input("solve for? (f, E1, E2): ").strip()
        if variable == "f":
            E1 = float(input("Enter E1: "))
            E2 = float(input("Enter E2: "))
            print(f"Frequency (f) = {(E1 - E2) / h} Hz")
        elif variable == "E1":
            f = float(input("Enter frequency (f): "))
            E2 = float(input("Enter E2: "))
            print(f"E1 = {h * f + E2} J")
        elif variable == "E2":
            f = float(input("Enter frequency (f): "))
            E1 = float(input("Enter E1: "))
            print(f"E2 = {E1 - h * f} J")
        else:
            print("Invalid variable choice")

    elif choice == "lambda=h/mv":
        variable = input("solve for? (lambda, m, v): ").strip()
        if variable == "lambda":
            m = float(input("Enter mass (m): "))
            v = float(input("Enter velocity (v): "))
            print(f"de Broglie wavelength (lambda) = {h / (m * v)} m")
        elif variable == "m":
            lam = float(input("Enter wavelength (lambda): "))
            v = float(input("Enter velocity (v): "))
            print(f"Mass (m) = {h / (lam * v)} kg")
        elif variable == "v":
            lam = float(input("Enter wavelength (lambda): "))
            m = float(input("Enter mass (m): "))
            print(f"Velocity (v) = {h / (lam * m)} m/s")
        else:
            print("Invalid variable choice")

    elif choice == "v=flambda":
        variable = input("solve for? (v, f, lambda): ").strip()
        if variable == "v":
            f = float(input("Enter frequency (f): "))
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Wave speed (v) = {f * lam}")
        elif variable == "f":
            v = float(input("Enter wave speed (v): "))
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Frequency (f) = {v / lam}")
        elif variable == "lambda":
            v = float(input("Enter wave speed (v): "))
            f = float(input("Enter frequency (f): "))
            print(f"Wavelength (lambda) = {v / f}")
        else:
            print("Invalid variable choice")

    elif choice == "f=1/T":
        variable = input("solve for? (f, T): ").strip()
        if variable == "f":
            T = float(input("Enter period (T): "))
            print(f"Frequency (f) = {1 / T}")
        elif variable == "T":
            f = float(input("Enter frequency (f): "))
            print(f"Period (T) = {1 / f}")
        else:
            print("Invalid variable choice")

    elif choice == "f=(1/2l)sqrt(T/mu)":
        variable = input("solve for? (f, l, T, mu): ").strip()
        if variable == "f":
            l = float(input("Enter length (l): "))
            T = float(input("Enter tension (T): "))
            mu = float(input("Enter mass per unit length (mu): "))
            print(f"First harmonic (f) = {(1 / (2 * l)) * math.sqrt(T / mu)}")
        elif variable == "l":
            f = float(input("Enter frequency (f): "))
            T = float(input("Enter tension (T): "))
            mu = float(input("Enter mass per unit length (mu): "))
            print(f"Length (l) = {(1 / (2 * f)) * math.sqrt(T / mu)}")
        elif variable == "T":
            f = float(input("Enter frequency (f): "))
            l = float(input("Enter length (l): "))
            mu = float(input("Enter mass per unit length (mu): "))
            print(f"Tension (T) = {mu * (2 * l * f)**2}")
        elif variable == "mu":
            f = float(input("Enter frequency (f): "))
            l = float(input("Enter length (l): "))
            T = float(input("Enter tension (T): "))
            print(f"Mass per unit length (mu) = {T / (2 * l * f)**2}")
        else:
            print("Invalid variable choice")

    elif choice == "w=lambdaD/s":
        variable = input("solve for? (w, lambda, D, s): ").strip()
        if variable == "w":
            lam = float(input("Enter wavelength (lambda): "))
            D = float(input("Enter slit-to-screen distance (D): "))
            s = float(input("Enter slit separation (s): "))
            print(f"Fringe spacing (w) = {lam * D / s}")
        elif variable == "lambda":
            w = float(input("Enter fringe spacing (w): "))
            D = float(input("Enter slit-to-screen distance (D): "))
            s = float(input("Enter slit separation (s): "))
            print(f"Wavelength (lambda) = {w * s / D}")
        elif variable == "D":
            w = float(input("Enter fringe spacing (w): "))
            lam = float(input("Enter wavelength (lambda): "))
            s = float(input("Enter slit separation (s): "))
            print(f"Slit-to-screen distance (D) = {w * s / lam}")
        elif variable == "s":
            w = float(input("Enter fringe spacing (w): "))
            lam = float(input("Enter wavelength (lambda): "))
            D = float(input("Enter slit-to-screen distance (D): "))
            print(f"Slit separation (s) = {lam * D / w}")
        else:
            print("Invalid variable choice")

    elif choice == "dsintheta=nlambda":
        variable = input("solve for? (d, theta, n, lambda): ").strip()
        if variable == "d":
            theta = float(input("Enter angle in degrees (theta): "))
            n = float(input("Enter order (n): "))
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Grating spacing (d) = {n * lam / math.sin(math.radians(theta))}")
        elif variable == "theta":
            d = float(input("Enter grating spacing (d): "))
            n = float(input("Enter order (n): "))
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Angle (theta) = {math.degrees(math.asin(n * lam / d))} degrees")
        elif variable == "n":
            d = float(input("Enter grating spacing (d): "))
            theta = float(input("Enter angle in degrees (theta): "))
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Order (n) = {d * math.sin(math.radians(theta)) / lam}")
        elif variable == "lambda":
            d = float(input("Enter grating spacing (d): "))
            theta = float(input("Enter angle in degrees (theta): "))
            n = float(input("Enter order (n): "))
            print(f"Wavelength (lambda) = {d * math.sin(math.radians(theta)) / n}")
        else:
            print("Invalid variable choice")

    elif choice == "n=c/cs":
        variable = input("solve for? (n, cs): ").strip()
        if variable == "n":
            cs = float(input("Enter speed of light in substance (cs): "))
            print(f"Refractive index (n) = {c / cs}")
        elif variable == "cs":
            n = float(input("Enter refractive index (n): "))
            print(f"Speed in substance (cs) = {c / n}")
        else:
            print("Invalid variable choice")

    elif choice == "n1sintheta1=n2sintheta2":
        variable = input("solve for? (theta1, theta2, n1, n2): ").strip()
        if variable == "theta2":
            n1 = float(input("Enter n1: "))
            theta1 = float(input("Enter angle 1 in degrees: "))
            n2 = float(input("Enter n2: "))
            print(f"Angle 2 (theta2) = {math.degrees(math.asin(n1 * math.sin(math.radians(theta1)) / n2))} degrees")
        elif variable == "theta1":
            n1 = float(input("Enter n1: "))
            n2 = float(input("Enter n2: "))
            theta2 = float(input("Enter angle 2 in degrees: "))
            print(f"Angle 1 (theta1) = {math.degrees(math.asin(n2 * math.sin(math.radians(theta2)) / n1))} degrees")
        elif variable == "n1":
            theta1 = float(input("Enter angle 1 in degrees: "))
            n2 = float(input("Enter n2: "))
            theta2 = float(input("Enter angle 2 in degrees: "))
            print(f"n1 = {n2 * math.sin(math.radians(theta2)) / math.sin(math.radians(theta1))}")
        elif variable == "n2":
            n1 = float(input("Enter n1: "))
            theta1 = float(input("Enter angle 1 in degrees: "))
            theta2 = float(input("Enter angle 2 in degrees: "))
            print(f"n2 = {n1 * math.sin(math.radians(theta1)) / math.sin(math.radians(theta2))}")
        else:
            print("Invalid variable choice")

    elif choice == "sinthetac=n2/n1":
        variable = input("solve for? (thetac, n1, n2): ").strip()
        if variable == "thetac":
            n2 = float(input("Enter n2: "))
            n1 = float(input("Enter n1: "))
            print(f"Critical angle (thetac) = {math.degrees(math.asin(n2 / n1))} degrees")
        elif variable == "n1":
            thetac = float(input("Enter critical angle in degrees: "))
            n2 = float(input("Enter n2: "))
            print(f"n1 = {n2 / math.sin(math.radians(thetac))}")
        elif variable == "n2":
            thetac = float(input("Enter critical angle in degrees: "))
            n1 = float(input("Enter n1: "))
            print(f"n2 = {n1 * math.sin(math.radians(thetac))}")
        else:
            print("Invalid variable choice")

   

    elif choice == "I=Q/t":
        variable = input("solve for? (I, Q, t): ").strip()
        if variable == "I":
            Q = float(input("Enter charge (Q): "))
            t = float(input("Enter time (t): "))
            print(f"Current (I) = {Q / t}")
        elif variable == "Q":
            I = float(input("Enter current (I): "))
            t = float(input("Enter time (t): "))
            print(f"Charge (Q) = {I * t}")
        elif variable == "t":
            I = float(input("Enter current (I): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Time (t) = {Q / I}")
        else:
            print("Invalid variable choice")

    elif choice == "V=W/Q":
        variable = input("solve for? (V, W, Q): ").strip()
        if variable == "V":
            W = float(input("Enter work/energy (W): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Potential difference (V) = {W / Q}")
        elif variable == "W":
            V = float(input("Enter pd (V): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Work/energy (W) = {V * Q}")
        elif variable == "Q":
            V = float(input("Enter pd (V): "))
            W = float(input("Enter work/energy (W): "))
            print(f"Charge (Q) = {W / V}")
        else:
            print("Invalid variable choice")

    elif choice == "R=V/I":
        variable = input("solve for? (R, V, I): ").strip()
        if variable == "R":
            V = float(input("Enter pd (V): "))
            I = float(input("Enter current (I): "))
            print(f"Resistance (R) = {V / I}")
        elif variable == "V":
            R = float(input("Enter resistance (R): "))
            I = float(input("Enter current (I): "))
            print(f"Potential difference (V) = {R * I}")
        elif variable == "I":
            R = float(input("Enter resistance (R): "))
            V = float(input("Enter pd (V): "))
            print(f"Current (I) = {V / R}")
        else:
            print("Invalid variable choice")

    elif choice == "rho=RA/L":
        variable = input("solve for? (rho, R, A, L): ").strip()
        if variable == "rho":
            R = float(input("Enter resistance (R): "))
            A = float(input("Enter cross-sectional area (A): "))
            L = float(input("Enter length (L): "))
            print(f"Resistivity (rho) = {R * A / L}")
        elif variable == "R":
            rho = float(input("Enter resistivity (rho): "))
            A = float(input("Enter cross-sectional area (A): "))
            L = float(input("Enter length (L): "))
            print(f"Resistance (R) = {rho * L / A}")
        elif variable == "A":
            rho = float(input("Enter resistivity (rho): "))
            R = float(input("Enter resistance (R): "))
            L = float(input("Enter length (L): "))
            print(f"Area (A) = {rho * L / R}")
        elif variable == "L":
            rho = float(input("Enter resistivity (rho): "))
            R = float(input("Enter resistance (R): "))
            A = float(input("Enter cross-sectional area (A): "))
            print(f"Length (L) = {R * A / rho}")
        else:
            print("Invalid variable choice")

    elif choice == "Rseries":
        n = int(input("How many resistors in series? "))
        total = 0.0
        for i in range(n):
            total += float(input(f"Enter resistance R{i + 1}: "))
        print(f"Total resistance (RT) = {total}")

    elif choice == "Rparallel":
        n = int(input("How many resistors in parallel? "))
        inv = 0.0
        for i in range(n):
            inv += 1 / float(input(f"Enter resistance R{i + 1}: "))
        print(f"Total resistance (RT) = {1 / inv}")

    elif choice == "P=VI":
        variable = input("solve for? (P, V, I): ").strip()
        if variable == "P":
            V = float(input("Enter pd (V): "))
            I = float(input("Enter current (I): "))
            print(f"Power (P) = {V * I}")
        elif variable == "V":
            P = float(input("Enter power (P): "))
            I = float(input("Enter current (I): "))
            print(f"Potential difference (V) = {P / I}")
        elif variable == "I":
            P = float(input("Enter power (P): "))
            V = float(input("Enter pd (V): "))
            print(f"Current (I) = {P / V}")
        else:
            print("Invalid variable choice")

    elif choice == "P=I^2R":
        variable = input("solve for? (P, I, R): ").strip()
        if variable == "P":
            I = float(input("Enter current (I): "))
            R = float(input("Enter resistance (R): "))
            print(f"Power (P) = {I**2 * R}")
        elif variable == "I":
            P = float(input("Enter power (P): "))
            R = float(input("Enter resistance (R): "))
            print(f"Current (I) = {math.sqrt(P / R)}")
        elif variable == "R":
            P = float(input("Enter power (P): "))
            I = float(input("Enter current (I): "))
            print(f"Resistance (R) = {P / I**2}")
        else:
            print("Invalid variable choice")

    elif choice == "P=V^2/R":
        variable = input("solve for? (P, V, R): ").strip()
        if variable == "P":
            V = float(input("Enter pd (V): "))
            R = float(input("Enter resistance (R): "))
            print(f"Power (P) = {V**2 / R}")
        elif variable == "V":
            P = float(input("Enter power (P): "))
            R = float(input("Enter resistance (R): "))
            print(f"Potential difference (V) = {math.sqrt(P * R)}")
        elif variable == "R":
            P = float(input("Enter power (P): "))
            V = float(input("Enter pd (V): "))
            print(f"Resistance (R) = {V**2 / P}")
        else:
            print("Invalid variable choice")

    elif choice == "emf=E/Q":
        variable = input("solve for? (emf, E, Q): ").strip()
        if variable == "emf":
            E = float(input("Enter energy (E): "))
            Q = float(input("Enter charge (Q): "))
            print(f"emf = {E / Q}")
        elif variable == "E":
            emf = float(input("Enter emf: "))
            Q = float(input("Enter charge (Q): "))
            print(f"Energy (E) = {emf * Q}")
        elif variable == "Q":
            emf = float(input("Enter emf: "))
            E = float(input("Enter energy (E): "))
            print(f"Charge (Q) = {E / emf}")
        else:
            print("Invalid variable choice")

    elif choice == "emf=I(R+r)":
        variable = input("solve for? (emf, I, R, r): ").strip()
        if variable == "emf":
            I = float(input("Enter current (I): "))
            R = float(input("Enter external resistance (R): "))
            r = float(input("Enter internal resistance (r): "))
            print(f"emf = {I * (R + r)}")
        elif variable == "I":
            emf = float(input("Enter emf: "))
            R = float(input("Enter external resistance (R): "))
            r = float(input("Enter internal resistance (r): "))
            print(f"Current (I) = {emf / (R + r)}")
        elif variable == "R":
            emf = float(input("Enter emf: "))
            I = float(input("Enter current (I): "))
            r = float(input("Enter internal resistance (r): "))
            print(f"External resistance (R) = {emf / I - r}")
        elif variable == "r":
            emf = float(input("Enter emf: "))
            I = float(input("Enter current (I): "))
            R = float(input("Enter external resistance (R): "))
            print(f"Internal resistance (r) = {emf / I - R}")
        else:
            print("Invalid variable choice")

    
    elif choice == "omega=v/r":
        variable = input("solve for? (omega, v, r): ").strip()
        if variable == "omega":
            v = float(input("Enter linear speed (v): "))
            r = float(input("Enter radius (r): "))
            print(f"Angular speed (omega) = {v / r}")
        elif variable == "v":
            omega = float(input("Enter angular speed (omega): "))
            r = float(input("Enter radius (r): "))
            print(f"Linear speed (v) = {omega * r}")
        elif variable == "r":
            omega = float(input("Enter angular speed (omega): "))
            v = float(input("Enter linear speed (v): "))
            print(f"Radius (r) = {v / omega}")
        else:
            print("Invalid variable choice")

    elif choice == "omega=2pif":
        variable = input("solve for? (omega, f): ").strip()
        if variable == "omega":
            f = float(input("Enter frequency (f): "))
            print(f"Angular speed (omega) = {2 * math.pi * f}")
        elif variable == "f":
            omega = float(input("Enter angular speed (omega): "))
            print(f"Frequency (f) = {omega / (2 * math.pi)}")
        else:
            print("Invalid variable choice")

    elif choice == "a=v^2/r":
        variable = input("solve for? (a, v, r): ").strip()
        if variable == "a":
            v = float(input("Enter linear speed (v): "))
            r = float(input("Enter radius (r): "))
            print(f"Centripetal acceleration (a) = {v**2 / r}")
        elif variable == "v":
            a = float(input("Enter acceleration (a): "))
            r = float(input("Enter radius (r): "))
            print(f"Linear speed (v) = {math.sqrt(a * r)}")
        elif variable == "r":
            a = float(input("Enter acceleration (a): "))
            v = float(input("Enter linear speed (v): "))
            print(f"Radius (r) = {v**2 / a}")
        else:
            print("Invalid variable choice")

    elif choice == "a=omega^2r":
        variable = input("solve for? (a, omega, r): ").strip()
        if variable == "a":
            omega = float(input("Enter angular speed (omega): "))
            r = float(input("Enter radius (r): "))
            print(f"Centripetal acceleration (a) = {omega**2 * r}")
        elif variable == "omega":
            a = float(input("Enter acceleration (a): "))
            r = float(input("Enter radius (r): "))
            print(f"Angular speed (omega) = {math.sqrt(a / r)}")
        elif variable == "r":
            a = float(input("Enter acceleration (a): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Radius (r) = {a / omega**2}")
        else:
            print("Invalid variable choice")

    elif choice == "F=mv^2/r":
        variable = input("solve for? (F, m, v, r): ").strip()
        if variable == "F":
            m = float(input("Enter mass (m): "))
            v = float(input("Enter linear speed (v): "))
            r = float(input("Enter radius (r): "))
            print(f"Centripetal force (F) = {m * v**2 / r}")
        elif variable == "m":
            F = float(input("Enter force (F): "))
            v = float(input("Enter linear speed (v): "))
            r = float(input("Enter radius (r): "))
            print(f"Mass (m) = {F * r / v**2}")
        elif variable == "v":
            F = float(input("Enter force (F): "))
            m = float(input("Enter mass (m): "))
            r = float(input("Enter radius (r): "))
            print(f"Linear speed (v) = {math.sqrt(F * r / m)}")
        elif variable == "r":
            F = float(input("Enter force (F): "))
            m = float(input("Enter mass (m): "))
            v = float(input("Enter linear speed (v): "))
            print(f"Radius (r) = {m * v**2 / F}")
        else:
            print("Invalid variable choice")

    elif choice == "F=momega^2r":
        variable = input("solve for? (F, m, omega, r): ").strip()
        if variable == "F":
            m = float(input("Enter mass (m): "))
            omega = float(input("Enter angular speed (omega): "))
            r = float(input("Enter radius (r): "))
            print(f"Centripetal force (F) = {m * omega**2 * r}")
        elif variable == "m":
            F = float(input("Enter force (F): "))
            omega = float(input("Enter angular speed (omega): "))
            r = float(input("Enter radius (r): "))
            print(f"Mass (m) = {F / (omega**2 * r)}")
        elif variable == "omega":
            F = float(input("Enter force (F): "))
            m = float(input("Enter mass (m): "))
            r = float(input("Enter radius (r): "))
            print(f"Angular speed (omega) = {math.sqrt(F / (m * r))}")
        elif variable == "r":
            F = float(input("Enter force (F): "))
            m = float(input("Enter mass (m): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Radius (r) = {F / (m * omega**2)}")
        else:
            print("Invalid variable choice")

    # =====================================================================
    # SIMPLE HARMONIC MOTION
    # =====================================================================
    elif choice == "a=-omega^2x":
        variable = input("solve for? (a, omega, x): ").strip()
        if variable == "a":
            omega = float(input("Enter angular frequency (omega): "))
            x = float(input("Enter displacement (x): "))
            print(f"Acceleration (a) = {-omega**2 * x}")
        elif variable == "omega":
            a = float(input("Enter acceleration (a): "))
            x = float(input("Enter displacement (x): "))
            print(f"Angular frequency (omega) = {math.sqrt(-a / x)}")
        elif variable == "x":
            a = float(input("Enter acceleration (a): "))
            omega = float(input("Enter angular frequency (omega): "))
            print(f"Displacement (x) = {-a / omega**2}")
        else:
            print("Invalid variable choice")

    elif choice == "x=Acos(omegat)":
        variable = input("solve for? (x, A, omega, t): ").strip()
        if variable == "x":
            A = float(input("Enter amplitude (A): "))
            omega = float(input("Enter angular frequency (omega): "))
            t = float(input("Enter time (t): "))
            print(f"Displacement (x) = {A * math.cos(omega * t)}")
        elif variable == "A":
            x = float(input("Enter displacement (x): "))
            omega = float(input("Enter angular frequency (omega): "))
            t = float(input("Enter time (t): "))
            print(f"Amplitude (A) = {x / math.cos(omega * t)}")
        elif variable == "omega":
            x = float(input("Enter displacement (x): "))
            A = float(input("Enter amplitude (A): "))
            t = float(input("Enter time (t): "))
            print(f"Angular frequency (omega) = {math.acos(x / A) / t}")
        elif variable == "t":
            x = float(input("Enter displacement (x): "))
            A = float(input("Enter amplitude (A): "))
            omega = float(input("Enter angular frequency (omega): "))
            print(f"Time (t) = {math.acos(x / A) / omega}")
        else:
            print("Invalid variable choice")

    elif choice == "v=omegasqrt(A^2-x^2)":
        variable = input("solve for? (v, omega, A, x): ").strip()
        if variable == "v":
            omega = float(input("Enter angular frequency (omega): "))
            A = float(input("Enter amplitude (A): "))
            x = float(input("Enter displacement (x): "))
            print(f"Speed (v) = {omega * math.sqrt(A**2 - x**2)}")
        elif variable == "omega":
            v = float(input("Enter speed (v): "))
            A = float(input("Enter amplitude (A): "))
            x = float(input("Enter displacement (x): "))
            print(f"Angular frequency (omega) = {v / math.sqrt(A**2 - x**2)}")
        elif variable == "A":
            v = float(input("Enter speed (v): "))
            omega = float(input("Enter angular frequency (omega): "))
            x = float(input("Enter displacement (x): "))
            print(f"Amplitude (A) = {math.sqrt((v / omega)**2 + x**2)}")
        elif variable == "x":
            v = float(input("Enter speed (v): "))
            omega = float(input("Enter angular frequency (omega): "))
            A = float(input("Enter amplitude (A): "))
            print(f"Displacement (x) = {math.sqrt(A**2 - (v / omega)**2)}")
        else:
            print("Invalid variable choice")

    elif choice == "vmax=omegaA":
        variable = input("solve for? (vmax, omega, A): ").strip()
        if variable == "vmax":
            omega = float(input("Enter angular frequency (omega): "))
            A = float(input("Enter amplitude (A): "))
            print(f"Maximum speed (vmax) = {omega * A}")
        elif variable == "omega":
            vmax = float(input("Enter maximum speed (vmax): "))
            A = float(input("Enter amplitude (A): "))
            print(f"Angular frequency (omega) = {vmax / A}")
        elif variable == "A":
            vmax = float(input("Enter maximum speed (vmax): "))
            omega = float(input("Enter angular frequency (omega): "))
            print(f"Amplitude (A) = {vmax / omega}")
        else:
            print("Invalid variable choice")

    elif choice == "amax=omega^2A":
        variable = input("solve for? (amax, omega, A): ").strip()
        if variable == "amax":
            omega = float(input("Enter angular frequency (omega): "))
            A = float(input("Enter amplitude (A): "))
            print(f"Maximum acceleration (amax) = {omega**2 * A}")
        elif variable == "omega":
            amax = float(input("Enter maximum acceleration (amax): "))
            A = float(input("Enter amplitude (A): "))
            print(f"Angular frequency (omega) = {math.sqrt(amax / A)}")
        elif variable == "A":
            amax = float(input("Enter maximum acceleration (amax): "))
            omega = float(input("Enter angular frequency (omega): "))
            print(f"Amplitude (A) = {amax / omega**2}")
        else:
            print("Invalid variable choice")

    elif choice == "T=2pisqrt(m/k)":
        variable = input("solve for? (T, m, k): ").strip()
        if variable == "T":
            m = float(input("Enter mass (m): "))
            k = float(input("Enter spring constant (k): "))
            print(f"Period (T) = {2 * math.pi * math.sqrt(m / k)}")
        elif variable == "m":
            T = float(input("Enter period (T): "))
            k = float(input("Enter spring constant (k): "))
            print(f"Mass (m) = {k * (T / (2 * math.pi))**2}")
        elif variable == "k":
            T = float(input("Enter period (T): "))
            m = float(input("Enter mass (m): "))
            print(f"Spring constant (k) = {m / (T / (2 * math.pi))**2}")
        else:
            print("Invalid variable choice")

    elif choice == "T=2pisqrt(l/g)":
        variable = input("solve for? (T, l, g): ").strip()
        if variable == "T":
            l = float(input("Enter length (l): "))
            g_in = float(input("Enter g (default 9.81): ") or g)
            print(f"Period (T) = {2 * math.pi * math.sqrt(l / g_in)}")
        elif variable == "l":
            T = float(input("Enter period (T): "))
            g_in = float(input("Enter g (default 9.81): ") or g)
            print(f"Length (l) = {g_in * (T / (2 * math.pi))**2}")
        elif variable == "g":
            T = float(input("Enter period (T): "))
            l = float(input("Enter length (l): "))
            print(f"g = {l / (T / (2 * math.pi))**2}")
        else:
            print("Invalid variable choice")

    

    elif choice == "Q=mcdtheta":
        variable = input("solve for? (Q, m, c, dtheta): ").strip()
        if variable == "Q":
            m = float(input("Enter mass (m): "))
            c_sh = float(input("Enter specific heat capacity (c): "))
            dtheta = float(input("Enter temperature change (dtheta): "))
            print(f"Energy (Q) = {m * c_sh * dtheta}")
        elif variable == "m":
            Q = float(input("Enter energy (Q): "))
            c_sh = float(input("Enter specific heat capacity (c): "))
            dtheta = float(input("Enter temperature change (dtheta): "))
            print(f"Mass (m) = {Q / (c_sh * dtheta)}")
        elif variable == "c":
            Q = float(input("Enter energy (Q): "))
            m = float(input("Enter mass (m): "))
            dtheta = float(input("Enter temperature change (dtheta): "))
            print(f"Specific heat capacity (c) = {Q / (m * dtheta)}")
        elif variable == "dtheta":
            Q = float(input("Enter energy (Q): "))
            m = float(input("Enter mass (m): "))
            c_sh = float(input("Enter specific heat capacity (c): "))
            print(f"Temperature change (dtheta) = {Q / (m * c_sh)}")
        else:
            print("Invalid variable choice")

    elif choice == "Q=ml":
        variable = input("solve for? (Q, m, l): ").strip()
        if variable == "Q":
            m = float(input("Enter mass (m): "))
            l = float(input("Enter specific latent heat (l): "))
            print(f"Energy (Q) = {m * l}")
        elif variable == "m":
            Q = float(input("Enter energy (Q): "))
            l = float(input("Enter specific latent heat (l): "))
            print(f"Mass (m) = {Q / l}")
        elif variable == "l":
            Q = float(input("Enter energy (Q): "))
            m = float(input("Enter mass (m): "))
            print(f"Specific latent heat (l) = {Q / m}")
        else:
            print("Invalid variable choice")

    elif choice == "pV=nRT":
        variable = input("solve for? (p, V, n, T): ").strip()
        if variable == "p":
            V = float(input("Enter volume (V): "))
            n = float(input("Enter number of moles (n): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Pressure (p) = {n * R_gas * T / V}")
        elif variable == "V":
            p = float(input("Enter pressure (p): "))
            n = float(input("Enter number of moles (n): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Volume (V) = {n * R_gas * T / p}")
        elif variable == "n":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Number of moles (n) = {p * V / (R_gas * T)}")
        elif variable == "T":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            n = float(input("Enter number of moles (n): "))
            print(f"Temperature (T) = {p * V / (n * R_gas)} K")
        else:
            print("Invalid variable choice")

    elif choice == "pV=NkT":
        variable = input("solve for? (p, V, N, T): ").strip()
        if variable == "p":
            V = float(input("Enter volume (V): "))
            N = float(input("Enter number of molecules (N): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Pressure (p) = {N * k_B * T / V}")
        elif variable == "V":
            p = float(input("Enter pressure (p): "))
            N = float(input("Enter number of molecules (N): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Volume (V) = {N * k_B * T / p}")
        elif variable == "N":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Number of molecules (N) = {p * V / (k_B * T)}")
        elif variable == "T":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            N = float(input("Enter number of molecules (N): "))
            print(f"Temperature (T) = {p * V / (N * k_B)} K")
        else:
            print("Invalid variable choice")

    elif choice == "pV=(1/3)Nmcrms^2":
        variable = input("solve for? (p, V, N, m, crms): ").strip()
        if variable == "p":
            V = float(input("Enter volume (V): "))
            N = float(input("Enter number of molecules (N): "))
            m = float(input("Enter molecule mass (m): "))
            crms = float(input("Enter rms speed (crms): "))
            print(f"Pressure (p) = {(1 / 3) * N * m * crms**2 / V}")
        elif variable == "crms":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            N = float(input("Enter number of molecules (N): "))
            m = float(input("Enter molecule mass (m): "))
            print(f"rms speed (crms) = {math.sqrt(3 * p * V / (N * m))}")
        elif variable == "N":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            m = float(input("Enter molecule mass (m): "))
            crms = float(input("Enter rms speed (crms): "))
            print(f"Number of molecules (N) = {3 * p * V / (m * crms**2)}")
        elif variable == "m":
            p = float(input("Enter pressure (p): "))
            V = float(input("Enter volume (V): "))
            N = float(input("Enter number of molecules (N): "))
            crms = float(input("Enter rms speed (crms): "))
            print(f"Molecule mass (m) = {3 * p * V / (N * crms**2)}")
        elif variable == "V":
            p = float(input("Enter pressure (p): "))
            N = float(input("Enter number of molecules (N): "))
            m = float(input("Enter molecule mass (m): "))
            crms = float(input("Enter rms speed (crms): "))
            print(f"Volume (V) = {(1 / 3) * N * m * crms**2 / p}")
        else:
            print("Invalid variable choice")

    elif choice == "0.5mcrms^2=1.5kT":
        variable = input("solve for? (crms, m, T): ").strip()
        if variable == "crms":
            m = float(input("Enter molecule mass (m): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"rms speed (crms) = {math.sqrt(3 * k_B * T / m)}")
        elif variable == "m":
            crms = float(input("Enter rms speed (crms): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Molecule mass (m) = {3 * k_B * T / crms**2}")
        elif variable == "T":
            crms = float(input("Enter rms speed (crms): "))
            m = float(input("Enter molecule mass (m): "))
            print(f"Temperature (T) = {m * crms**2 / (3 * k_B)} K")
        else:
            print("Invalid variable choice")

    # =====================================================================
    # GRAVITATIONAL FIELDS
    # =====================================================================
    elif choice == "F=Gm1m2/r^2":
        variable = input("solve for? (F, m1, m2, r): ").strip()
        if variable == "F":
            m1 = float(input("Enter mass 1 (m1): "))
            m2 = float(input("Enter mass 2 (m2): "))
            r = float(input("Enter separation (r): "))
            print(f"Force (F) = {G * m1 * m2 / r**2}")
        elif variable == "m1":
            F = float(input("Enter force (F): "))
            m2 = float(input("Enter mass 2 (m2): "))
            r = float(input("Enter separation (r): "))
            print(f"Mass 1 (m1) = {F * r**2 / (G * m2)}")
        elif variable == "m2":
            F = float(input("Enter force (F): "))
            m1 = float(input("Enter mass 1 (m1): "))
            r = float(input("Enter separation (r): "))
            print(f"Mass 2 (m2) = {F * r**2 / (G * m1)}")
        elif variable == "r":
            F = float(input("Enter force (F): "))
            m1 = float(input("Enter mass 1 (m1): "))
            m2 = float(input("Enter mass 2 (m2): "))
            print(f"Separation (r) = {math.sqrt(G * m1 * m2 / F)}")
        else:
            print("Invalid variable choice")

    elif choice == "g=F/m":
        variable = input("solve for? (g, F, m): ").strip()
        if variable == "g":
            F = float(input("Enter force (F): "))
            m = float(input("Enter mass (m): "))
            print(f"Field strength (g) = {F / m}")
        elif variable == "F":
            g_val = float(input("Enter field strength (g): "))
            m = float(input("Enter mass (m): "))
            print(f"Force (F) = {g_val * m}")
        elif variable == "m":
            g_val = float(input("Enter field strength (g): "))
            F = float(input("Enter force (F): "))
            print(f"Mass (m) = {F / g_val}")
        else:
            print("Invalid variable choice")

    elif choice == "g=GM/r^2":
        variable = input("solve for? (g, M, r): ").strip()
        if variable == "g":
            M = float(input("Enter mass (M): "))
            r = float(input("Enter distance (r): "))
            print(f"Field strength (g) = {G * M / r**2}")
        elif variable == "M":
            g_val = float(input("Enter field strength (g): "))
            r = float(input("Enter distance (r): "))
            print(f"Mass (M) = {g_val * r**2 / G}")
        elif variable == "r":
            g_val = float(input("Enter field strength (g): "))
            M = float(input("Enter mass (M): "))
            print(f"Distance (r) = {math.sqrt(G * M / g_val)}")
        else:
            print("Invalid variable choice")

    elif choice == "dW=mdV":
        variable = input("solve for? (dW, m, dV): ").strip()
        if variable == "dW":
            m = float(input("Enter mass (m): "))
            dV = float(input("Enter change in potential (dV): "))
            print(f"Work done (dW) = {m * dV}")
        elif variable == "m":
            dW = float(input("Enter work done (dW): "))
            dV = float(input("Enter change in potential (dV): "))
            print(f"Mass (m) = {dW / dV}")
        elif variable == "dV":
            dW = float(input("Enter work done (dW): "))
            m = float(input("Enter mass (m): "))
            print(f"Change in potential (dV) = {dW / m}")
        else:
            print("Invalid variable choice")

    elif choice == "Vgrav=-GM/r":
        variable = input("solve for? (V, M, r): ").strip()
        if variable == "V":
            M = float(input("Enter mass (M): "))
            r = float(input("Enter distance (r): "))
            print(f"Gravitational potential (V) = {-G * M / r}")
        elif variable == "M":
            V = float(input("Enter potential (V): "))
            r = float(input("Enter distance (r): "))
            print(f"Mass (M) = {-V * r / G}")
        elif variable == "r":
            V = float(input("Enter potential (V): "))
            M = float(input("Enter mass (M): "))
            print(f"Distance (r) = {-G * M / V}")
        else:
            print("Invalid variable choice")

    
    elif choice == "F=Q1Q2/4pie0r^2":
        variable = input("solve for? (F, Q1, Q2, r): ").strip()
        if variable == "F":
            Q1 = float(input("Enter charge 1 (Q1): "))
            Q2 = float(input("Enter charge 2 (Q2): "))
            r = float(input("Enter separation (r): "))
            print(f"Force (F) = {Q1 * Q2 / (4 * math.pi * e0 * r**2)}")
        elif variable == "Q1":
            F = float(input("Enter force (F): "))
            Q2 = float(input("Enter charge 2 (Q2): "))
            r = float(input("Enter separation (r): "))
            print(f"Charge 1 (Q1) = {F * 4 * math.pi * e0 * r**2 / Q2}")
        elif variable == "Q2":
            F = float(input("Enter force (F): "))
            Q1 = float(input("Enter charge 1 (Q1): "))
            r = float(input("Enter separation (r): "))
            print(f"Charge 2 (Q2) = {F * 4 * math.pi * e0 * r**2 / Q1}")
        elif variable == "r":
            F = float(input("Enter force (F): "))
            Q1 = float(input("Enter charge 1 (Q1): "))
            Q2 = float(input("Enter charge 2 (Q2): "))
            print(f"Separation (r) = {math.sqrt(Q1 * Q2 / (4 * math.pi * e0 * F))}")
        else:
            print("Invalid variable choice")

    elif choice == "F=EQ":
        variable = input("solve for? (F, E, Q): ").strip()
        if variable == "F":
            E = float(input("Enter field strength (E): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Force (F) = {E * Q}")
        elif variable == "E":
            F = float(input("Enter force (F): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Field strength (E) = {F / Q}")
        elif variable == "Q":
            F = float(input("Enter force (F): "))
            E = float(input("Enter field strength (E): "))
            print(f"Charge (Q) = {F / E}")
        else:
            print("Invalid variable choice")

    elif choice == "E=V/d":
        variable = input("solve for? (E, V, d): ").strip()
        if variable == "E":
            V = float(input("Enter pd (V): "))
            d = float(input("Enter separation (d): "))
            print(f"Field strength (E) = {V / d}")
        elif variable == "V":
            E = float(input("Enter field strength (E): "))
            d = float(input("Enter separation (d): "))
            print(f"Potential difference (V) = {E * d}")
        elif variable == "d":
            E = float(input("Enter field strength (E): "))
            V = float(input("Enter pd (V): "))
            print(f"Separation (d) = {V / E}")
        else:
            print("Invalid variable choice")

    elif choice == "dW=QdV":
        variable = input("solve for? (dW, Q, dV): ").strip()
        if variable == "dW":
            Q = float(input("Enter charge (Q): "))
            dV = float(input("Enter change in potential (dV): "))
            print(f"Work done (dW) = {Q * dV}")
        elif variable == "Q":
            dW = float(input("Enter work done (dW): "))
            dV = float(input("Enter change in potential (dV): "))
            print(f"Charge (Q) = {dW / dV}")
        elif variable == "dV":
            dW = float(input("Enter work done (dW): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Change in potential (dV) = {dW / Q}")
        else:
            print("Invalid variable choice")

    elif choice == "E=Q/4pie0r^2":
        variable = input("solve for? (E, Q, r): ").strip()
        if variable == "E":
            Q = float(input("Enter charge (Q): "))
            r = float(input("Enter distance (r): "))
            print(f"Field strength (E) = {Q / (4 * math.pi * e0 * r**2)}")
        elif variable == "Q":
            E = float(input("Enter field strength (E): "))
            r = float(input("Enter distance (r): "))
            print(f"Charge (Q) = {E * 4 * math.pi * e0 * r**2}")
        elif variable == "r":
            E = float(input("Enter field strength (E): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Distance (r) = {math.sqrt(Q / (4 * math.pi * e0 * E))}")
        else:
            print("Invalid variable choice")

    elif choice == "Velec=Q/4pie0r":
        variable = input("solve for? (V, Q, r): ").strip()
        if variable == "V":
            Q = float(input("Enter charge (Q): "))
            r = float(input("Enter distance (r): "))
            print(f"Electric potential (V) = {Q / (4 * math.pi * e0 * r)}")
        elif variable == "Q":
            V = float(input("Enter potential (V): "))
            r = float(input("Enter distance (r): "))
            print(f"Charge (Q) = {V * 4 * math.pi * e0 * r}")
        elif variable == "r":
            V = float(input("Enter potential (V): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Distance (r) = {Q / (4 * math.pi * e0 * V)}")
        else:
            print("Invalid variable choice")

    elif choice == "C=Q/V":
        variable = input("solve for? (C, Q, V): ").strip()
        if variable == "C":
            Q = float(input("Enter charge (Q): "))
            V = float(input("Enter pd (V): "))
            print(f"Capacitance (C) = {Q / V}")
        elif variable == "Q":
            C = float(input("Enter capacitance (C): "))
            V = float(input("Enter pd (V): "))
            print(f"Charge (Q) = {C * V}")
        elif variable == "V":
            C = float(input("Enter capacitance (C): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Potential difference (V) = {Q / C}")
        else:
            print("Invalid variable choice")

    elif choice == "C=Ae0er/d":
        variable = input("solve for? (C, A, er, d): ").strip()
        if variable == "C":
            A = float(input("Enter plate area (A): "))
            er = float(input("Enter relative permittivity (er): "))
            d = float(input("Enter plate separation (d): "))
            print(f"Capacitance (C) = {A * e0 * er / d}")
        elif variable == "A":
            C = float(input("Enter capacitance (C): "))
            er = float(input("Enter relative permittivity (er): "))
            d = float(input("Enter plate separation (d): "))
            print(f"Plate area (A) = {C * d / (e0 * er)}")
        elif variable == "er":
            C = float(input("Enter capacitance (C): "))
            A = float(input("Enter plate area (A): "))
            d = float(input("Enter plate separation (d): "))
            print(f"Relative permittivity (er) = {C * d / (e0 * A)}")
        elif variable == "d":
            C = float(input("Enter capacitance (C): "))
            A = float(input("Enter plate area (A): "))
            er = float(input("Enter relative permittivity (er): "))
            print(f"Plate separation (d) = {A * e0 * er / C}")
        else:
            print("Invalid variable choice")

    elif choice == "E=0.5QV":
        variable = input("solve for? (E, Q, V): ").strip()
        if variable == "E":
            Q = float(input("Enter charge (Q): "))
            V = float(input("Enter pd (V): "))
            print(f"Energy stored (E) = {0.5 * Q * V}")
        elif variable == "Q":
            E = float(input("Enter energy (E): "))
            V = float(input("Enter pd (V): "))
            print(f"Charge (Q) = {2 * E / V}")
        elif variable == "V":
            E = float(input("Enter energy (E): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Potential difference (V) = {2 * E / Q}")
        else:
            print("Invalid variable choice")

    elif choice == "E=0.5CV^2":
        variable = input("solve for? (E, C, V): ").strip()
        if variable == "E":
            C = float(input("Enter capacitance (C): "))
            V = float(input("Enter pd (V): "))
            print(f"Energy stored (E) = {0.5 * C * V**2}")
        elif variable == "C":
            E = float(input("Enter energy (E): "))
            V = float(input("Enter pd (V): "))
            print(f"Capacitance (C) = {2 * E / V**2}")
        elif variable == "V":
            E = float(input("Enter energy (E): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Potential difference (V) = {math.sqrt(2 * E / C)}")
        else:
            print("Invalid variable choice")

    elif choice == "E=0.5Q^2/C":
        variable = input("solve for? (E, Q, C): ").strip()
        if variable == "E":
            Q = float(input("Enter charge (Q): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Energy stored (E) = {0.5 * Q**2 / C}")
        elif variable == "Q":
            E = float(input("Enter energy (E): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Charge (Q) = {math.sqrt(2 * E * C)}")
        elif variable == "C":
            E = float(input("Enter energy (E): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Capacitance (C) = {0.5 * Q**2 / E}")
        else:
            print("Invalid variable choice")

    elif choice == "Q=Q0(1-e^-t/RC)":
        variable = input("solve for? (Q, Q0, t): ").strip()
        if variable == "Q":
            Q0 = float(input("Enter initial/max charge (Q0): "))
            t = float(input("Enter time (t): "))
            R = float(input("Enter resistance (R): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Charge (Q) = {Q0 * (1 - math.exp(-t / (R * C)))}")
        elif variable == "Q0":
            Q = float(input("Enter charge (Q): "))
            t = float(input("Enter time (t): "))
            R = float(input("Enter resistance (R): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Max charge (Q0) = {Q / (1 - math.exp(-t / (R * C)))}")
        elif variable == "t":
            Q = float(input("Enter charge (Q): "))
            Q0 = float(input("Enter max charge (Q0): "))
            R = float(input("Enter resistance (R): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Time (t) = {-R * C * math.log(1 - Q / Q0)}")
        else:
            print("Invalid variable choice")

    elif choice == "Q=Q0e^-t/RC":
        variable = input("solve for? (Q, Q0, t): ").strip()
        if variable == "Q":
            Q0 = float(input("Enter initial charge (Q0): "))
            t = float(input("Enter time (t): "))
            R = float(input("Enter resistance (R): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Charge (Q) = {Q0 * math.exp(-t / (R * C))}")
        elif variable == "Q0":
            Q = float(input("Enter charge (Q): "))
            t = float(input("Enter time (t): "))
            R = float(input("Enter resistance (R): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Initial charge (Q0) = {Q / math.exp(-t / (R * C))}")
        elif variable == "t":
            Q = float(input("Enter charge (Q): "))
            Q0 = float(input("Enter initial charge (Q0): "))
            R = float(input("Enter resistance (R): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Time (t) = {-R * C * math.log(Q / Q0)}")
        else:
            print("Invalid variable choice")


    elif choice == "F=BIl":
        variable = input("solve for? (F, B, I, l): ").strip()
        if variable == "F":
            B = float(input("Enter flux density (B): "))
            I = float(input("Enter current (I): "))
            l = float(input("Enter length (l): "))
            print(f"Force (F) = {B * I * l}")
        elif variable == "B":
            F = float(input("Enter force (F): "))
            I = float(input("Enter current (I): "))
            l = float(input("Enter length (l): "))
            print(f"Flux density (B) = {F / (I * l)}")
        elif variable == "I":
            F = float(input("Enter force (F): "))
            B = float(input("Enter flux density (B): "))
            l = float(input("Enter length (l): "))
            print(f"Current (I) = {F / (B * l)}")
        elif variable == "l":
            F = float(input("Enter force (F): "))
            B = float(input("Enter flux density (B): "))
            I = float(input("Enter current (I): "))
            print(f"Length (l) = {F / (B * I)}")
        else:
            print("Invalid variable choice")

    elif choice == "F=BQv":
        variable = input("solve for? (F, B, Q, v): ").strip()
        if variable == "F":
            B = float(input("Enter flux density (B): "))
            Q = float(input("Enter charge (Q): "))
            v = float(input("Enter velocity (v): "))
            print(f"Force (F) = {B * Q * v}")
        elif variable == "B":
            F = float(input("Enter force (F): "))
            Q = float(input("Enter charge (Q): "))
            v = float(input("Enter velocity (v): "))
            print(f"Flux density (B) = {F / (Q * v)}")
        elif variable == "Q":
            F = float(input("Enter force (F): "))
            B = float(input("Enter flux density (B): "))
            v = float(input("Enter velocity (v): "))
            print(f"Charge (Q) = {F / (B * v)}")
        elif variable == "v":
            F = float(input("Enter force (F): "))
            B = float(input("Enter flux density (B): "))
            Q = float(input("Enter charge (Q): "))
            print(f"Velocity (v) = {F / (B * Q)}")
        else:
            print("Invalid variable choice")

    elif choice == "flux=BA":
        variable = input("solve for? (flux, B, A): ").strip()
        if variable == "flux":
            B = float(input("Enter flux density (B): "))
            A = float(input("Enter area (A): "))
            print(f"Magnetic flux = {B * A}")
        elif variable == "B":
            flux = float(input("Enter magnetic flux: "))
            A = float(input("Enter area (A): "))
            print(f"Flux density (B) = {flux / A}")
        elif variable == "A":
            flux = float(input("Enter magnetic flux: "))
            B = float(input("Enter flux density (B): "))
            print(f"Area (A) = {flux / B}")
        else:
            print("Invalid variable choice")

    elif choice == "fluxlinkage=BANcostheta":
        variable = input("solve for? (linkage, B, A, N, theta): ").strip()
        if variable == "linkage":
            B = float(input("Enter flux density (B): "))
            A = float(input("Enter area (A): "))
            N = float(input("Enter number of turns (N): "))
            theta = float(input("Enter angle in degrees (theta): "))
            print(f"Flux linkage = {B * A * N * math.cos(math.radians(theta))}")
        elif variable == "B":
            linkage = float(input("Enter flux linkage: "))
            A = float(input("Enter area (A): "))
            N = float(input("Enter number of turns (N): "))
            theta = float(input("Enter angle in degrees (theta): "))
            print(f"Flux density (B) = {linkage / (A * N * math.cos(math.radians(theta)))}")
        elif variable == "theta":
            linkage = float(input("Enter flux linkage: "))
            B = float(input("Enter flux density (B): "))
            A = float(input("Enter area (A): "))
            N = float(input("Enter number of turns (N): "))
            print(f"Angle (theta) = {math.degrees(math.acos(linkage / (B * A * N)))} degrees")
        else:
            print("Invalid variable choice")

    elif choice == "emf=NdPhi/dt":
        variable = input("solve for? (emf, N, dPhi, dt): ").strip()
        if variable == "emf":
            N = float(input("Enter number of turns (N): "))
            dPhi = float(input("Enter change in flux (dPhi): "))
            dt = float(input("Enter time (dt): "))
            print(f"Induced emf = {N * dPhi / dt}")
        elif variable == "N":
            emf = float(input("Enter emf: "))
            dPhi = float(input("Enter change in flux (dPhi): "))
            dt = float(input("Enter time (dt): "))
            print(f"Number of turns (N) = {emf * dt / dPhi}")
        elif variable == "dPhi":
            emf = float(input("Enter emf: "))
            N = float(input("Enter number of turns (N): "))
            dt = float(input("Enter time (dt): "))
            print(f"Change in flux (dPhi) = {emf * dt / N}")
        elif variable == "dt":
            emf = float(input("Enter emf: "))
            N = float(input("Enter number of turns (N): "))
            dPhi = float(input("Enter change in flux (dPhi): "))
            print(f"Time (dt) = {N * dPhi / emf}")
        else:
            print("Invalid variable choice")

    elif choice == "emf=BANomegasin":
        variable = input("solve for? (emf, B, A, N, omega, t): ").strip()
        B = float(input("Enter flux density (B): "))
        A = float(input("Enter area (A): "))
        N = float(input("Enter number of turns (N): "))
        omega = float(input("Enter angular speed (omega): "))
        t = float(input("Enter time (t): "))
        print(f"Induced emf = {B * A * N * omega * math.sin(omega * t)}")

    elif choice == "Irms=I0/sqrt2":
        variable = input("solve for? (Irms, I0): ").strip()
        if variable == "Irms":
            I0 = float(input("Enter peak current (I0): "))
            print(f"RMS current (Irms) = {I0 / math.sqrt(2)}")
        elif variable == "I0":
            Irms = float(input("Enter RMS current (Irms): "))
            print(f"Peak current (I0) = {Irms * math.sqrt(2)}")
        else:
            print("Invalid variable choice")

    elif choice == "Vrms=V0/sqrt2":
        variable = input("solve for? (Vrms, V0): ").strip()
        if variable == "Vrms":
            V0 = float(input("Enter peak voltage (V0): "))
            print(f"RMS voltage (Vrms) = {V0 / math.sqrt(2)}")
        elif variable == "V0":
            Vrms = float(input("Enter RMS voltage (Vrms): "))
            print(f"Peak voltage (V0) = {Vrms * math.sqrt(2)}")
        else:
            print("Invalid variable choice")

    elif choice == "Ns/Np=Vs/Vp":
        variable = input("solve for? (Ns, Np, Vs, Vp): ").strip()
        if variable == "Ns":
            Np = float(input("Enter primary turns (Np): "))
            Vs = float(input("Enter secondary voltage (Vs): "))
            Vp = float(input("Enter primary voltage (Vp): "))
            print(f"Secondary turns (Ns) = {Np * Vs / Vp}")
        elif variable == "Np":
            Ns = float(input("Enter secondary turns (Ns): "))
            Vs = float(input("Enter secondary voltage (Vs): "))
            Vp = float(input("Enter primary voltage (Vp): "))
            print(f"Primary turns (Np) = {Ns * Vp / Vs}")
        elif variable == "Vs":
            Ns = float(input("Enter secondary turns (Ns): "))
            Np = float(input("Enter primary turns (Np): "))
            Vp = float(input("Enter primary voltage (Vp): "))
            print(f"Secondary voltage (Vs) = {Ns * Vp / Np}")
        elif variable == "Vp":
            Ns = float(input("Enter secondary turns (Ns): "))
            Np = float(input("Enter primary turns (Np): "))
            Vs = float(input("Enter secondary voltage (Vs): "))
            print(f"Primary voltage (Vp) = {Np * Vs / Ns}")
        else:
            print("Invalid variable choice")

    elif choice == "transformereff":
        Is = float(input("Enter secondary current (Is): "))
        Vs = float(input("Enter secondary voltage (Vs): "))
        Ip = float(input("Enter primary current (Ip): "))
        Vp = float(input("Enter primary voltage (Vp): "))
        eff = (Is * Vs) / (Ip * Vp)
        print(f"Transformer efficiency = {eff}  ({eff * 100} %)")

    
    elif choice == "I=k/x^2":
        variable = input("solve for? (I, k, x): ").strip()
        if variable == "I":
            k_const = float(input("Enter constant (k): "))
            x = float(input("Enter distance (x): "))
            print(f"Intensity (I) = {k_const / x**2}")
        elif variable == "k":
            I = float(input("Enter intensity (I): "))
            x = float(input("Enter distance (x): "))
            print(f"Constant (k) = {I * x**2}")
        elif variable == "x":
            I = float(input("Enter intensity (I): "))
            k_const = float(input("Enter constant (k): "))
            print(f"Distance (x) = {math.sqrt(k_const / I)}")
        else:
            print("Invalid variable choice")

    elif choice == "N=N0e^-lambdat":
        variable = input("solve for? (N, N0, lambda, t): ").strip()
        if variable == "N":
            N0 = float(input("Enter initial number (N0): "))
            lam = float(input("Enter decay constant (lambda): "))
            t = float(input("Enter time (t): "))
            print(f"Number remaining (N) = {N0 * math.exp(-lam * t)}")
        elif variable == "N0":
            N = float(input("Enter number remaining (N): "))
            lam = float(input("Enter decay constant (lambda): "))
            t = float(input("Enter time (t): "))
            print(f"Initial number (N0) = {N / math.exp(-lam * t)}")
        elif variable == "lambda":
            N = float(input("Enter number remaining (N): "))
            N0 = float(input("Enter initial number (N0): "))
            t = float(input("Enter time (t): "))
            print(f"Decay constant (lambda) = {-math.log(N / N0) / t}")
        elif variable == "t":
            N = float(input("Enter number remaining (N): "))
            N0 = float(input("Enter initial number (N0): "))
            lam = float(input("Enter decay constant (lambda): "))
            print(f"Time (t) = {-math.log(N / N0) / lam}")
        else:
            print("Invalid variable choice")

    elif choice == "A=lambdaN":
        variable = input("solve for? (A, lambda, N): ").strip()
        if variable == "A":
            lam = float(input("Enter decay constant (lambda): "))
            N = float(input("Enter number of nuclei (N): "))
            print(f"Activity (A) = {lam * N}")
        elif variable == "lambda":
            A = float(input("Enter activity (A): "))
            N = float(input("Enter number of nuclei (N): "))
            print(f"Decay constant (lambda) = {A / N}")
        elif variable == "N":
            A = float(input("Enter activity (A): "))
            lam = float(input("Enter decay constant (lambda): "))
            print(f"Number of nuclei (N) = {A / lam}")
        else:
            print("Invalid variable choice")

    elif choice == "halflife":
        variable = input("solve for? (halflife, lambda): ").strip()
        if variable == "halflife":
            lam = float(input("Enter decay constant (lambda): "))
            print(f"Half-life = {math.log(2) / lam}")
        elif variable == "lambda":
            T_half = float(input("Enter half-life: "))
            print(f"Decay constant (lambda) = {math.log(2) / T_half}")
        else:
            print("Invalid variable choice")

    elif choice == "R=R0A^(1/3)":
        variable = input("solve for? (R, R0, A): ").strip()
        if variable == "R":
            R0 = float(input("Enter R0 (approx 1.2e-15): "))
            A = float(input("Enter nucleon number (A): "))
            print(f"Nuclear radius (R) = {R0 * A**(1 / 3)}")
        elif variable == "R0":
            R = float(input("Enter nuclear radius (R): "))
            A = float(input("Enter nucleon number (A): "))
            print(f"R0 = {R / A**(1 / 3)}")
        elif variable == "A":
            R = float(input("Enter nuclear radius (R): "))
            R0 = float(input("Enter R0 (approx 1.2e-15): "))
            print(f"Nucleon number (A) = {(R / R0)**3}")
        else:
            print("Invalid variable choice")

    elif choice == "E=mc^2":
        variable = input("solve for? (E, m): ").strip()
        if variable == "E":
            m = float(input("Enter mass (m): "))
            print(f"Energy (E) = {m * c**2} J")
        elif variable == "m":
            E = float(input("Enter energy (E): "))
            print(f"Mass (m) = {E / c**2} kg")
        else:
            print("Invalid variable choice")


    elif choice == "M=f0/fe":
        variable = input("solve for? (M, f0, fe): ").strip()
        if variable == "M":
            f0 = float(input("Enter objective focal length (f0): "))
            fe = float(input("Enter eyepiece focal length (fe): "))
            print(f"Angular magnification (M) = {f0 / fe}")
        elif variable == "f0":
            M = float(input("Enter magnification (M): "))
            fe = float(input("Enter eyepiece focal length (fe): "))
            print(f"Objective focal length (f0) = {M * fe}")
        elif variable == "fe":
            M = float(input("Enter magnification (M): "))
            f0 = float(input("Enter objective focal length (f0): "))
            print(f"Eyepiece focal length (fe) = {f0 / M}")
        else:
            print("Invalid variable choice")

    elif choice == "theta=lambda/D":
        variable = input("solve for? (theta, lambda, D): ").strip()
        if variable == "theta":
            lam = float(input("Enter wavelength (lambda): "))
            D = float(input("Enter aperture diameter (D): "))
            print(f"Resolving angle (theta) = {lam / D} rad")
        elif variable == "lambda":
            theta = float(input("Enter angle in radians (theta): "))
            D = float(input("Enter aperture diameter (D): "))
            print(f"Wavelength (lambda) = {theta * D}")
        elif variable == "D":
            theta = float(input("Enter angle in radians (theta): "))
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Aperture diameter (D) = {lam / theta}")
        else:
            print("Invalid variable choice")

    elif choice == "m-M=5log(d/10)":
        variable = input("solve for? (m, M, d): ").strip()
        if variable == "m":
            M = float(input("Enter absolute magnitude (M): "))
            d = float(input("Enter distance in parsecs (d): "))
            print(f"Apparent magnitude (m) = {M + 5 * math.log10(d / 10)}")
        elif variable == "M":
            m = float(input("Enter apparent magnitude (m): "))
            d = float(input("Enter distance in parsecs (d): "))
            print(f"Absolute magnitude (M) = {m - 5 * math.log10(d / 10)}")
        elif variable == "d":
            m = float(input("Enter apparent magnitude (m): "))
            M = float(input("Enter absolute magnitude (M): "))
            print(f"Distance (d) = {10 * 10**((m - M) / 5)} parsecs")
        else:
            print("Invalid variable choice")

    elif choice == "lambdamaxT=2.9e-3":
        variable = input("solve for? (lambdamax, T): ").strip()
        if variable == "lambdamax":
            T = float(input("Enter temperature in K (T): "))
            print(f"Peak wavelength (lambdamax) = {2.9e-3 / T} m")
        elif variable == "T":
            lam = float(input("Enter peak wavelength (lambdamax): "))
            print(f"Temperature (T) = {2.9e-3 / lam} K")
        else:
            print("Invalid variable choice")

    elif choice == "P=sigmaAT^4":
        variable = input("solve for? (P, A, T): ").strip()
        if variable == "P":
            A = float(input("Enter surface area (A): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Power (P) = {sigma * A * T**4}")
        elif variable == "A":
            P = float(input("Enter power (P): "))
            T = float(input("Enter temperature in K (T): "))
            print(f"Surface area (A) = {P / (sigma * T**4)}")
        elif variable == "T":
            P = float(input("Enter power (P): "))
            A = float(input("Enter surface area (A): "))
            print(f"Temperature (T) = {(P / (sigma * A))**0.25} K")
        else:
            print("Invalid variable choice")

    elif choice == "Rs=2GM/c^2":
        variable = input("solve for? (Rs, M): ").strip()
        if variable == "Rs":
            M = float(input("Enter mass (M): "))
            print(f"Schwarzschild radius (Rs) = {2 * G * M / c**2} m")
        elif variable == "M":
            Rs = float(input("Enter Schwarzschild radius (Rs): "))
            print(f"Mass (M) = {Rs * c**2 / (2 * G)} kg")
        else:
            print("Invalid variable choice")

    elif choice == "z=v/c":
        variable = input("solve for? (z, v): ").strip()
        if variable == "z":
            v = float(input("Enter recession velocity (v): "))
            print(f"Red shift (z) = {v / c}")
        elif variable == "v":
            z = float(input("Enter red shift (z): "))
            print(f"Recession velocity (v) = {z * c} m/s")
        else:
            print("Invalid variable choice")

    elif choice == "v=Hd":
        variable = input("solve for? (v, H, d): ").strip()
        if variable == "v":
            H = float(input("Enter Hubble constant (H): "))
            d = float(input("Enter distance (d): "))
            print(f"Recession velocity (v) = {H * d}")
        elif variable == "H":
            v = float(input("Enter recession velocity (v): "))
            d = float(input("Enter distance (d): "))
            print(f"Hubble constant (H) = {v / d}")
        elif variable == "d":
            v = float(input("Enter recession velocity (v): "))
            H = float(input("Enter Hubble constant (H): "))
            print(f"Distance (d) = {v / H}")
        else:
            print("Invalid variable choice")

    elif choice == "P=1/f":
        variable = input("solve for? (P, f): ").strip()
        if variable == "P":
            f = float(input("Enter focal length (f): "))
            print(f"Lens power (P) = {1 / f} D")
        elif variable == "f":
            P = float(input("Enter lens power (P): "))
            print(f"Focal length (f) = {1 / P} m")
        else:
            print("Invalid variable choice")

    elif choice == "m=v/u":
        variable = input("solve for? (m, v, u): ").strip()
        if variable == "m":
            v = float(input("Enter image distance (v): "))
            u = float(input("Enter object distance (u): "))
            print(f"Magnification (m) = {v / u}")
        elif variable == "v":
            m = float(input("Enter magnification (m): "))
            u = float(input("Enter object distance (u): "))
            print(f"Image distance (v) = {m * u}")
        elif variable == "u":
            m = float(input("Enter magnification (m): "))
            v = float(input("Enter image distance (v): "))
            print(f"Object distance (u) = {v / m}")
        else:
            print("Invalid variable choice")

    elif choice == "1/f=1/u+1/v":
        variable = input("solve for? (f, u, v): ").strip()
        if variable == "f":
            u = float(input("Enter object distance (u): "))
            v = float(input("Enter image distance (v): "))
            print(f"Focal length (f) = {1 / (1 / u + 1 / v)}")
        elif variable == "u":
            f = float(input("Enter focal length (f): "))
            v = float(input("Enter image distance (v): "))
            print(f"Object distance (u) = {1 / (1 / f - 1 / v)}")
        elif variable == "v":
            f = float(input("Enter focal length (f): "))
            u = float(input("Enter object distance (u): "))
            print(f"Image distance (v) = {1 / (1 / f - 1 / u)}")
        else:
            print("Invalid variable choice")

    elif choice == "level=10log(I/I0)":
        I0 = 1.0e-12  # threshold of hearing (W m^-2)
        variable = input("solve for? (level, I): ").strip()
        if variable == "level":
            I = float(input("Enter intensity (I): "))
            print(f"Intensity level = {10 * math.log10(I / I0)} dB")
        elif variable == "I":
            level = float(input("Enter intensity level in dB: "))
            print(f"Intensity (I) = {I0 * 10**(level / 10)} W/m^2")
        else:
            print("Invalid variable choice")

    elif choice == "I=I0e^-mux":
        variable = input("solve for? (I, I0, mu, x): ").strip()
        if variable == "I":
            I0 = float(input("Enter incident intensity (I0): "))
            mu = float(input("Enter attenuation coefficient (mu): "))
            x = float(input("Enter thickness (x): "))
            print(f"Transmitted intensity (I) = {I0 * math.exp(-mu * x)}")
        elif variable == "I0":
            I = float(input("Enter transmitted intensity (I): "))
            mu = float(input("Enter attenuation coefficient (mu): "))
            x = float(input("Enter thickness (x): "))
            print(f"Incident intensity (I0) = {I / math.exp(-mu * x)}")
        elif variable == "mu":
            I = float(input("Enter transmitted intensity (I): "))
            I0 = float(input("Enter incident intensity (I0): "))
            x = float(input("Enter thickness (x): "))
            print(f"Attenuation coefficient (mu) = {-math.log(I / I0) / x}")
        elif variable == "x":
            I = float(input("Enter transmitted intensity (I): "))
            I0 = float(input("Enter incident intensity (I0): "))
            mu = float(input("Enter attenuation coefficient (mu): "))
            print(f"Thickness (x) = {-math.log(I / I0) / mu}")
        else:
            print("Invalid variable choice")

    elif choice == "mum=mu/rho":
        variable = input("solve for? (mum, mu, rho): ").strip()
        if variable == "mum":
            mu = float(input("Enter attenuation coefficient (mu): "))
            rho = float(input("Enter density (rho): "))
            print(f"Mass attenuation coefficient (mum) = {mu / rho}")
        elif variable == "mu":
            mum = float(input("Enter mass attenuation coefficient (mum): "))
            rho = float(input("Enter density (rho): "))
            print(f"Attenuation coefficient (mu) = {mum * rho}")
        elif variable == "rho":
            mum = float(input("Enter mass attenuation coefficient (mum): "))
            mu = float(input("Enter attenuation coefficient (mu): "))
            print(f"Density (rho) = {mu / mum}")
        else:
            print("Invalid variable choice")

    elif choice == "Z=rhoc":
        variable = input("solve for? (Z, rho, cs): ").strip()
        if variable == "Z":
            rho = float(input("Enter density (rho): "))
            cs = float(input("Enter speed of sound in medium (cs): "))
            print(f"Acoustic impedance (Z) = {rho * cs}")
        elif variable == "rho":
            Z = float(input("Enter acoustic impedance (Z): "))
            cs = float(input("Enter speed of sound in medium (cs): "))
            print(f"Density (rho) = {Z / cs}")
        elif variable == "cs":
            Z = float(input("Enter acoustic impedance (Z): "))
            rho = float(input("Enter density (rho): "))
            print(f"Speed of sound (cs) = {Z / rho}")
        else:
            print("Invalid variable choice")

    elif choice == "1/TE=1/TB+1/TP":
        variable = input("solve for? (TE, TB, TP): ").strip()
        if variable == "TE":
            TB = float(input("Enter biological half-life (TB): "))
            TP = float(input("Enter physical half-life (TP): "))
            print(f"Effective half-life (TE) = {1 / (1 / TB + 1 / TP)}")
        elif variable == "TB":
            TE = float(input("Enter effective half-life (TE): "))
            TP = float(input("Enter physical half-life (TP): "))
            print(f"Biological half-life (TB) = {1 / (1 / TE - 1 / TP)}")
        elif variable == "TP":
            TE = float(input("Enter effective half-life (TE): "))
            TB = float(input("Enter biological half-life (TB): "))
            print(f"Physical half-life (TP) = {1 / (1 / TE - 1 / TB)}")
        else:
            print("Invalid variable choice")


    elif choice == "I=mr^2":
        variable = input("solve for? (I, m, r): ").strip()
        if variable == "I":
            m = float(input("Enter mass (m): "))
            r = float(input("Enter distance from axis (r): "))
            print(f"Moment of inertia (I) = {m * r**2}")
        elif variable == "m":
            I = float(input("Enter moment of inertia (I): "))
            r = float(input("Enter distance from axis (r): "))
            print(f"Mass (m) = {I / r**2}")
        elif variable == "r":
            I = float(input("Enter moment of inertia (I): "))
            m = float(input("Enter mass (m): "))
            print(f"Distance from axis (r) = {math.sqrt(I / m)}")
        else:
            print("Invalid variable choice")

    elif choice == "Ek=0.5Iomega^2":
        variable = input("solve for? (Ek, I, omega): ").strip()
        if variable == "Ek":
            I = float(input("Enter moment of inertia (I): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Angular kinetic energy (Ek) = {0.5 * I * omega**2}")
        elif variable == "I":
            Ek = float(input("Enter angular kinetic energy (Ek): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Moment of inertia (I) = {2 * Ek / omega**2}")
        elif variable == "omega":
            Ek = float(input("Enter angular kinetic energy (Ek): "))
            I = float(input("Enter moment of inertia (I): "))
            print(f"Angular speed (omega) = {math.sqrt(2 * Ek / I)}")
        else:
            print("Invalid variable choice")

    elif choice == "omega2=omega1+alphat":
        variable = input("solve for? (omega2, omega1, alpha, t): ").strip()
        if variable == "omega2":
            omega1 = float(input("Enter initial angular speed (omega1): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            t = float(input("Enter time (t): "))
            print(f"Final angular speed (omega2) = {omega1 + alpha * t}")
        elif variable == "omega1":
            omega2 = float(input("Enter final angular speed (omega2): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            t = float(input("Enter time (t): "))
            print(f"Initial angular speed (omega1) = {omega2 - alpha * t}")
        elif variable == "alpha":
            omega2 = float(input("Enter final angular speed (omega2): "))
            omega1 = float(input("Enter initial angular speed (omega1): "))
            t = float(input("Enter time (t): "))
            print(f"Angular acceleration (alpha) = {(omega2 - omega1) / t}")
        elif variable == "t":
            omega2 = float(input("Enter final angular speed (omega2): "))
            omega1 = float(input("Enter initial angular speed (omega1): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            print(f"Time (t) = {(omega2 - omega1) / alpha}")
        else:
            print("Invalid variable choice")

    elif choice == "omega2^2=omega1^2+2alphatheta":
        variable = input("solve for? (omega2, omega1, alpha, theta): ").strip()
        if variable == "omega2":
            omega1 = float(input("Enter initial angular speed (omega1): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            theta = float(input("Enter angle in radians (theta): "))
            print(f"Final angular speed (omega2) = {math.sqrt(omega1**2 + 2 * alpha * theta)}")
        elif variable == "omega1":
            omega2 = float(input("Enter final angular speed (omega2): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            theta = float(input("Enter angle in radians (theta): "))
            print(f"Initial angular speed (omega1) = {math.sqrt(omega2**2 - 2 * alpha * theta)}")
        elif variable == "alpha":
            omega2 = float(input("Enter final angular speed (omega2): "))
            omega1 = float(input("Enter initial angular speed (omega1): "))
            theta = float(input("Enter angle in radians (theta): "))
            print(f"Angular acceleration (alpha) = {(omega2**2 - omega1**2) / (2 * theta)}")
        elif variable == "theta":
            omega2 = float(input("Enter final angular speed (omega2): "))
            omega1 = float(input("Enter initial angular speed (omega1): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            print(f"Angle (theta) = {(omega2**2 - omega1**2) / (2 * alpha)}")
        else:
            print("Invalid variable choice")

    elif choice == "theta=omega1t+0.5alphat^2":
        variable = input("solve for? (theta, omega1, alpha, t): ").strip()
        if variable == "theta":
            omega1 = float(input("Enter initial angular speed (omega1): "))
            t = float(input("Enter time (t): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            print(f"Angle (theta) = {omega1 * t + 0.5 * alpha * t**2}")
        elif variable == "omega1":
            theta = float(input("Enter angle (theta): "))
            t = float(input("Enter time (t): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            print(f"Initial angular speed (omega1) = {(theta - 0.5 * alpha * t**2) / t}")
        elif variable == "alpha":
            theta = float(input("Enter angle (theta): "))
            omega1 = float(input("Enter initial angular speed (omega1): "))
            t = float(input("Enter time (t): "))
            print(f"Angular acceleration (alpha) = {2 * (theta - omega1 * t) / t**2}")
        else:
            print("Invalid variable choice")

    elif choice == "T=Ialpha":
        variable = input("solve for? (T, I, alpha): ").strip()
        if variable == "T":
            I = float(input("Enter moment of inertia (I): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            print(f"Torque (T) = {I * alpha}")
        elif variable == "I":
            T = float(input("Enter torque (T): "))
            alpha = float(input("Enter angular acceleration (alpha): "))
            print(f"Moment of inertia (I) = {T / alpha}")
        elif variable == "alpha":
            T = float(input("Enter torque (T): "))
            I = float(input("Enter moment of inertia (I): "))
            print(f"Angular acceleration (alpha) = {T / I}")
        else:
            print("Invalid variable choice")

    elif choice == "T=Fr":
        variable = input("solve for? (T, F, r): ").strip()
        if variable == "T":
            F = float(input("Enter force (F): "))
            r = float(input("Enter radius (r): "))
            print(f"Torque (T) = {F * r}")
        elif variable == "F":
            T = float(input("Enter torque (T): "))
            r = float(input("Enter radius (r): "))
            print(f"Force (F) = {T / r}")
        elif variable == "r":
            T = float(input("Enter torque (T): "))
            F = float(input("Enter force (F): "))
            print(f"Radius (r) = {T / F}")
        else:
            print("Invalid variable choice")

    elif choice == "L=Iomega":
        variable = input("solve for? (L, I, omega): ").strip()
        if variable == "L":
            I = float(input("Enter moment of inertia (I): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Angular momentum (L) = {I * omega}")
        elif variable == "I":
            L = float(input("Enter angular momentum (L): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Moment of inertia (I) = {L / omega}")
        elif variable == "omega":
            L = float(input("Enter angular momentum (L): "))
            I = float(input("Enter moment of inertia (I): "))
            print(f"Angular speed (omega) = {L / I}")
        else:
            print("Invalid variable choice")

    elif choice == "W=Ttheta":
        variable = input("solve for? (W, T, theta): ").strip()
        if variable == "W":
            T = float(input("Enter torque (T): "))
            theta = float(input("Enter angle in radians (theta): "))
            print(f"Work done (W) = {T * theta}")
        elif variable == "T":
            W = float(input("Enter work done (W): "))
            theta = float(input("Enter angle in radians (theta): "))
            print(f"Torque (T) = {W / theta}")
        elif variable == "theta":
            W = float(input("Enter work done (W): "))
            T = float(input("Enter torque (T): "))
            print(f"Angle (theta) = {W / T}")
        else:
            print("Invalid variable choice")

    elif choice == "P=Tomega":
        variable = input("solve for? (P, T, omega): ").strip()
        if variable == "P":
            T = float(input("Enter torque (T): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Power (P) = {T * omega}")
        elif variable == "T":
            P = float(input("Enter power (P): "))
            omega = float(input("Enter angular speed (omega): "))
            print(f"Torque (T) = {P / omega}")
        elif variable == "omega":
            P = float(input("Enter power (P): "))
            T = float(input("Enter torque (T): "))
            print(f"Angular speed (omega) = {P / T}")
        else:
            print("Invalid variable choice")

    elif choice == "Q=dU+W":
        variable = input("solve for? (Q, dU, W): ").strip()
        if variable == "Q":
            dU = float(input("Enter change in internal energy (dU): "))
            W = float(input("Enter work done (W): "))
            print(f"Heat energy (Q) = {dU + W}")
        elif variable == "dU":
            Q = float(input("Enter heat energy (Q): "))
            W = float(input("Enter work done (W): "))
            print(f"Change in internal energy (dU) = {Q - W}")
        elif variable == "W":
            Q = float(input("Enter heat energy (Q): "))
            dU = float(input("Enter change in internal energy (dU): "))
            print(f"Work done (W) = {Q - dU}")
        else:
            print("Invalid variable choice")

    elif choice == "W=pdV":
        variable = input("solve for? (W, p, dV): ").strip()
        if variable == "W":
            p = float(input("Enter pressure (p): "))
            dV = float(input("Enter change in volume (dV): "))
            print(f"Work done (W) = {p * dV}")
        elif variable == "p":
            W = float(input("Enter work done (W): "))
            dV = float(input("Enter change in volume (dV): "))
            print(f"Pressure (p) = {W / dV}")
        elif variable == "dV":
            W = float(input("Enter work done (W): "))
            p = float(input("Enter pressure (p): "))
            print(f"Change in volume (dV) = {W / p}")
        else:
            print("Invalid variable choice")

    elif choice == "engineeff":
        QH = float(input("Enter heat input (QH): "))
        QC = float(input("Enter heat rejected (QC): "))
        eff = (QH - QC) / QH
        print(f"Heat engine efficiency = {eff}  ({eff * 100} %)")

    elif choice == "maxeff":
        TH = float(input("Enter hot reservoir temperature in K (TH): "))
        TC = float(input("Enter cold reservoir temperature in K (TC): "))
        eff = (TH - TC) / TH
        print(f"Maximum theoretical efficiency = {eff}  ({eff * 100} %)")

    elif choice == "COPref":
        QC = float(input("Enter heat extracted (QC): "))
        QH = float(input("Enter heat rejected (QH): "))
        print(f"Refrigerator COP = {QC / (QH - QC)}")

    elif choice == "COPhp":
        QH = float(input("Enter heat delivered (QH): "))
        QC = float(input("Enter heat extracted (QC): "))
        print(f"Heat pump COP = {QH / (QH - QC)}")

    # =====================================================================
    # TURNING POINTS IN PHYSICS
    # =====================================================================
    elif choice == "F=eV/d":
        variable = input("solve for? (F, V, d): ").strip()
        if variable == "F":
            V = float(input("Enter pd (V): "))
            d = float(input("Enter plate separation (d): "))
            print(f"Force (F) = {e * V / d}")
        elif variable == "V":
            F = float(input("Enter force (F): "))
            d = float(input("Enter plate separation (d): "))
            print(f"Potential difference (V) = {F * d / e}")
        elif variable == "d":
            F = float(input("Enter force (F): "))
            V = float(input("Enter pd (V): "))
            print(f"Plate separation (d) = {e * V / F}")
        else:
            print("Invalid variable choice")

    elif choice == "F=Bev":
        variable = input("solve for? (F, B, v): ").strip()
        if variable == "F":
            B = float(input("Enter flux density (B): "))
            v = float(input("Enter velocity (v): "))
            print(f"Force (F) = {B * e * v}")
        elif variable == "B":
            F = float(input("Enter force (F): "))
            v = float(input("Enter velocity (v): "))
            print(f"Flux density (B) = {F / (e * v)}")
        elif variable == "v":
            F = float(input("Enter force (F): "))
            B = float(input("Enter flux density (B): "))
            print(f"Velocity (v) = {F / (B * e)}")
        else:
            print("Invalid variable choice")

    elif choice == "r=mv/Be":
        variable = input("solve for? (r, m, v, B): ").strip()
        if variable == "r":
            m = float(input("Enter mass (m): "))
            v = float(input("Enter velocity (v): "))
            B = float(input("Enter flux density (B): "))
            print(f"Radius (r) = {m * v / (B * e)}")
        elif variable == "m":
            r = float(input("Enter radius (r): "))
            v = float(input("Enter velocity (v): "))
            B = float(input("Enter flux density (B): "))
            print(f"Mass (m) = {r * B * e / v}")
        elif variable == "v":
            r = float(input("Enter radius (r): "))
            m = float(input("Enter mass (m): "))
            B = float(input("Enter flux density (B): "))
            print(f"Velocity (v) = {r * B * e / m}")
        elif variable == "B":
            r = float(input("Enter radius (r): "))
            m = float(input("Enter mass (m): "))
            v = float(input("Enter velocity (v): "))
            print(f"Flux density (B) = {m * v / (r * e)}")
        else:
            print("Invalid variable choice")

    elif choice == "0.5mv^2=eV":
        variable = input("solve for? (v, m, V): ").strip()
        if variable == "v":
            m = float(input("Enter mass (m): "))
            V = float(input("Enter accelerating pd (V): "))
            print(f"Velocity (v) = {math.sqrt(2 * e * V / m)}")
        elif variable == "m":
            v = float(input("Enter velocity (v): "))
            V = float(input("Enter accelerating pd (V): "))
            print(f"Mass (m) = {2 * e * V / v**2}")
        elif variable == "V":
            v = float(input("Enter velocity (v): "))
            m = float(input("Enter mass (m): "))
            print(f"Accelerating pd (V) = {0.5 * m * v**2 / e}")
        else:
            print("Invalid variable choice")

    elif choice == "QV/d=mg":
        variable = input("solve for? (Q, V, d, m): ").strip()
        if variable == "Q":
            V = float(input("Enter pd (V): "))
            d = float(input("Enter plate separation (d): "))
            m = float(input("Enter mass of drop (m): "))
            print(f"Charge (Q) = {m * g * d / V}")
        elif variable == "V":
            Q = float(input("Enter charge (Q): "))
            d = float(input("Enter plate separation (d): "))
            m = float(input("Enter mass of drop (m): "))
            print(f"Potential difference (V) = {m * g * d / Q}")
        elif variable == "d":
            Q = float(input("Enter charge (Q): "))
            V = float(input("Enter pd (V): "))
            m = float(input("Enter mass of drop (m): "))
            print(f"Plate separation (d) = {Q * V / (m * g)}")
        elif variable == "m":
            Q = float(input("Enter charge (Q): "))
            V = float(input("Enter pd (V): "))
            d = float(input("Enter plate separation (d): "))
            print(f"Mass of drop (m) = {Q * V / (d * g)}")
        else:
            print("Invalid variable choice")

    elif choice == "F=6pietarv":
        variable = input("solve for? (F, eta, r, v): ").strip()
        if variable == "F":
            eta = float(input("Enter viscosity (eta): "))
            r = float(input("Enter radius (r): "))
            v = float(input("Enter velocity (v): "))
            print(f"Drag force (F) = {6 * math.pi * eta * r * v}")
        elif variable == "eta":
            F = float(input("Enter drag force (F): "))
            r = float(input("Enter radius (r): "))
            v = float(input("Enter velocity (v): "))
            print(f"Viscosity (eta) = {F / (6 * math.pi * r * v)}")
        elif variable == "r":
            F = float(input("Enter drag force (F): "))
            eta = float(input("Enter viscosity (eta): "))
            v = float(input("Enter velocity (v): "))
            print(f"Radius (r) = {F / (6 * math.pi * eta * v)}")
        elif variable == "v":
            F = float(input("Enter drag force (F): "))
            eta = float(input("Enter viscosity (eta): "))
            r = float(input("Enter radius (r): "))
            print(f"Velocity (v) = {F / (6 * math.pi * eta * r)}")
        else:
            print("Invalid variable choice")

    elif choice == "lambda=h/sqrt(2meV)":
        variable = input("solve for? (lambda, V): ").strip()
        if variable == "lambda":
            V = float(input("Enter accelerating pd (V): "))
            print(f"Wavelength (lambda) = {h / math.sqrt(2 * me * e * V)} m")
        elif variable == "V":
            lam = float(input("Enter wavelength (lambda): "))
            print(f"Accelerating pd (V) = {h**2 / (2 * me * e * lam**2)} V")
        else:
            print("Invalid variable choice")

    elif choice == "t=t0/sqrt(1-v^2/c^2)":
        variable = input("solve for? (t, t0, v): ").strip()
        if variable == "t":
            t0 = float(input("Enter proper time (t0): "))
            v = float(input("Enter velocity (v): "))
            print(f"Dilated time (t) = {t0 / math.sqrt(1 - v**2 / c**2)}")
        elif variable == "t0":
            t = float(input("Enter dilated time (t): "))
            v = float(input("Enter velocity (v): "))
            print(f"Proper time (t0) = {t * math.sqrt(1 - v**2 / c**2)}")
        elif variable == "v":
            t = float(input("Enter dilated time (t): "))
            t0 = float(input("Enter proper time (t0): "))
            print(f"Velocity (v) = {c * math.sqrt(1 - (t0 / t)**2)} m/s")
        else:
            print("Invalid variable choice")

    elif choice == "l=l0sqrt(1-v^2/c^2)":
        variable = input("solve for? (l, l0, v): ").strip()
        if variable == "l":
            l0 = float(input("Enter proper length (l0): "))
            v = float(input("Enter velocity (v): "))
            print(f"Contracted length (l) = {l0 * math.sqrt(1 - v**2 / c**2)}")
        elif variable == "l0":
            l = float(input("Enter contracted length (l): "))
            v = float(input("Enter velocity (v): "))
            print(f"Proper length (l0) = {l / math.sqrt(1 - v**2 / c**2)}")
        elif variable == "v":
            l = float(input("Enter contracted length (l): "))
            l0 = float(input("Enter proper length (l0): "))
            print(f"Velocity (v) = {c * math.sqrt(1 - (l / l0)**2)} m/s")
        else:
            print("Invalid variable choice")


    elif choice == "f0=1/2pisqrt(LC)":
        variable = input("solve for? (f0, L, C): ").strip()
        if variable == "f0":
            L = float(input("Enter inductance (L): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Resonant frequency (f0) = {1 / (2 * math.pi * math.sqrt(L * C))}")
        elif variable == "L":
            f0 = float(input("Enter resonant frequency (f0): "))
            C = float(input("Enter capacitance (C): "))
            print(f"Inductance (L) = {1 / (C * (2 * math.pi * f0)**2)}")
        elif variable == "C":
            f0 = float(input("Enter resonant frequency (f0): "))
            L = float(input("Enter inductance (L): "))
            print(f"Capacitance (C) = {1 / (L * (2 * math.pi * f0)**2)}")
        else:
            print("Invalid variable choice")

    elif choice == "Q=f0/fB":
        variable = input("solve for? (Q, f0, fB): ").strip()
        if variable == "Q":
            f0 = float(input("Enter resonant frequency (f0): "))
            fB = float(input("Enter bandwidth (fB): "))
            print(f"Q-factor = {f0 / fB}")
        elif variable == "f0":
            Q = float(input("Enter Q-factor: "))
            fB = float(input("Enter bandwidth (fB): "))
            print(f"Resonant frequency (f0) = {Q * fB}")
        elif variable == "fB":
            Q = float(input("Enter Q-factor: "))
            f0 = float(input("Enter resonant frequency (f0): "))
            print(f"Bandwidth (fB) = {f0 / Q}")
        else:
            print("Invalid variable choice")

    else:
        print("That equation is in the menu but doesn't have a solver yet.")
