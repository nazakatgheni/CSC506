from tkinter import Tk
from ui import PortfolioUI


def main():
    root = Tk()
    app = PortfolioUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()