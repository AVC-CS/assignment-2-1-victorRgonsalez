def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """


    int_male = int(input("please enter the amount of males in your class \t"))
    int_female = int(input("please enter the amount of females in your class \t"))
    total = int_male + int_female

    def percentage(x):
        return  (x * 100) / total
    

    print(f'Total number of students: \t {total}')
    print(f'The number of males and females: \t {int_male} {int_female}')
    m_perc = percentage(int_male)
    f_perc = percentage(int_female)
    print(f'The percentage of males and females: \t {m_perc:.2f} {f_perc:.2f}')
    

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
