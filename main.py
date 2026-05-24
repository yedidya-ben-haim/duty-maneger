"""
מערכת ניהול תורנויות חיילים
"""
from soldier_manager import *
from utils import *
import data


# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================

def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.

    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)

    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("""===Welcome to the Soldier Management System===
                Please select from the menu:
                
                1.Adding a new soldier.
                2.Removing a soldier
                3.View soldiers
                4.Adding a duty to a soldier
                5.Duty status update
                6.View soldier duties
                7.exit
            """)


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש

    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    user_input = str(input("Please enter a choice>  "))
    return user_input


def handle_add_soldier(soldier_list: list) -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """

    is_soldier_added = False

    while not is_soldier_added:
        id_input = input("Please enter a soldier id>  ").strip()

        if not is_valid_id(id_input):
            print("ID must be 6-8 digits long. Please try again. ❌")
            print("-" * 40)
            continue

        soldier_id = int(id_input)
        name = input("Please enter the soldier name>  ")

        try:
            add_soldier(soldier_id, name, soldier_list)
            print("The soldier successfully added.✓")
            is_soldier_added = True

        except ValueError as e:
            print(f"error: {e}")
            print("Please try again with different details.\n")
            print("-" * 40)



def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("Please enter a soldier id>  "))

    try:
        remove_soldier(soldier_id)
        print("The soldier successfully removed.✓")
    except ValueError as e:
        print(f"error: {e}")


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    pass


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    soldiers_list = data.soldiers_list
    duties_list = data.soldiers_list
    pass

if __name__ == '__main__':
    main()