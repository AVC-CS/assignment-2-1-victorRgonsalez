def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    m_perc = int(input("please enter the amount of males in your class \t"))
    f_perc = int(input("please enter the amount of females in your class \t"))

    print(f'Total number of students: \t {m_perc + f_perc}')
    print(f'The number of males and females: \t {m_perc} {f_perc}')

    sum_m = (m_perc * 100) / (m_perc + f_perc)
    sum_f = (f_perc * 100) / (m_perc + f_perc)
    print(f'The percentage of males and females: \t {sum_m:.2f} {sum_f:.2f}')
    m_perc = sum_m
    f_perc = sum_f

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
