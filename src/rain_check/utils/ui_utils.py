def center_window(ctk, width, height):
    ctk.update_idletasks()
    screen_width = ctk.winfo_screenwidth()
    screen_height = ctk.winfo_screenheight()

    # Calculate the center position
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    ctk.geometry(f"{width}x{height}+{x}+{y}")