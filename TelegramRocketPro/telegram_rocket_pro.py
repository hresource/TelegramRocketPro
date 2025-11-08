# At the TOP after imports
import tkinter.messagebox as messagebox

# === AUTO-UPDATE ON START ===
if __name__ == "__main__":
    try:
        from updater import check_for_update
        check_for_update()
    except Exception as e:
        print(f"[UPDATE ERROR] {e}")

    # ... rest of main