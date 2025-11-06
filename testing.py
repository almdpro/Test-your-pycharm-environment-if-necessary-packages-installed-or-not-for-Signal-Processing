import sys
import platform

# --- Script to check if all core assignment libraries are installed ---

REQUIRED_LIBRARIES = {
    "pandas": "For data loading and handling.",
    "numpy": "For array manipulation and numerical operations.",
    "scipy": "For core DSP functions (filtering, correlation, etc.).",
    "matplotlib": "For plotting and visualization."
}


def check_all_installations():
    """
    Attempts to import all required libraries, reports status and version.
    """
    print("--- PyCharm Environment Check: DSP Assignment Libraries ---")
    all_installed = True

    missing_packages = []

    # Check each required DSP library
    for pkg_name, purpose in REQUIRED_LIBRARIES.items():
        try:
            # Dynamically import the package
            pkg = __import__(pkg_name)
            version = getattr(pkg, '__version__', 'Version not found')

            print(f"✅ SUCCESS: {pkg_name.upper()} is installed. (Version: {version})")

        except ImportError:
            print(f"❌ ERROR: {pkg_name.upper()} is NOT installed.")
            missing_packages.append(pkg_name)
            all_installed = False
        except Exception as e:
            print(f"⚠️ WARNING: Error loading {pkg_name}: {e}")

    # --- Check for the GUI Library (tkinter) ---
    print("\n--- GUI Library Check (Part 5) ---")
    try:
        # Check standard Tkinter import path
        import tkinter
        print(f"✅ SUCCESS: TKINTER (GUI) is installed.")
        # Attempt to get Tkinter version information
        try:
            # Tkinter version is usually derived from the underlying Tcl/Tk libraries
            print(f"   Tk version: {tkinter.Tcl().eval('info patchlevel')}")
        except:
            print("   Tkinter version information unavailable.")

    except ImportError:
        # This is rare, as Tkinter is usually bundled with Python
        print("❌ ERROR: TKINTER (GUI) is NOT found. This is unusual.")
        print("   On some systems, it requires installing the 'python-tk' package.")
        all_installed = False
    except Exception as e:
        # Catch any other unexpected errors during import
        print(f"⚠️ WARNING: Error loading TKINTER: {e}")

    print("\n-------------------------------------------------------")

    if all_installed:
        print("✅ ALL REQUIRED LIBRARIES ARE INSTALLED.")
        print("You are ready to run your full assignment code!")
    else:
        print("❌ MISSING PACKAGES DETECTED.")
        print("\nTo fix this, install the missing packages in your PyCharm project terminal:")

        # Print combined installation command
        install_command = "pip install " + " ".join(missing_packages)
        # Only print pip install command for standard packages, not tkinter
        if missing_packages:
            print(f"\n   {install_command}")

        print("\nAfter successful installation, please re-run this script to verify.")


if __name__ == "__main__":
    check_all_installations()
