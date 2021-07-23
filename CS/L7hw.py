def calc_bmi(weight, height):
    return (weight)/(height ** 2)

def eval_who_bmi(bmi):
    if bmi < 18.5:
        return "cân năng thấp(gầy)"
    elif bmi < 24.9:
        return "bình thường"
    elif bmi < 29.9:
        return "thừa cân"
    elif bmi < 34.9:
        return "béo phì độ I"
    elif bmi < 39.9:
        return "béo phì độ II"
    else:
        return "béo phì độ III"

def eval_idi_bmi(bmi):
    if bmi < 18.5:
        return "cân năng thấp(gầy)"
    elif bmi < 22.9:
        return "bình thường"
    elif bmi < 24.9:
        return "thừa cân"
    elif bmi < 29.9:
        return "béo phì độ I"
    elif bmi < 34.9:
        return "béo phì độ II"
    else:
        return "béo phì độ III"

def main():
    weight = float(input("1.Weight: "))
    height = float(input("Height: "))
    bmi = calc_bmi(weight, height)
    user_choice = str(input("Bạn muốn tính bmi theo công thức who hay idi? ")).lower()
    if user_choice == "who":
        print(eval_who_bmi(bmi))
    elif user_choice == "idi":
        print(eval_idi_bmi(bmi))

main()

