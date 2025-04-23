# main.py
from UniQuantumSense_face_detection import load_image, run_quantum_circuit_qiskit

def main():

    # Start the face detection application
    load_image()  # This will invoke the GUI for loading images

    # run quantum circuit logic here
    # run_quantum_circuit_qiskit()

if __name__ == "__main__":
    main()