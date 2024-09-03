def main():
    SP = 67.83643
    RJ = 36.67866
    MG = 29.22988
    ES = 27.36388
    Outros = 19.84953
    Total = SP + RJ + MG + ES + Outros

    Percentual_SP = round((SP*100)/Total, 2)
    Percentual_RJ = round((RJ*100)/Total, 2)
    Percentual_MG = round((MG*100)/(Total), 2)
    Percentual_ES = round((ES*100)/(Total), 2)
    Percentual_Outros = round((Outros*100)/(Total), 2)

    print("Percentual de SP: ", Percentual_SP, "%")
    print("Percentual de RJ: ", Percentual_RJ, "%")
    print("Percentual de MG: ", Percentual_MG, "%")
    print("Percentual de ES: ", Percentual_ES, "%")
    print("Percentual de Outros: ", Percentual_Outros, "%")


if __name__ == "__main__":
    main()
