pokracovat = "ano"
while pokracovat == "ano":
    print("")
    print("Vítejte v našem dotazníku o vás. Zeptáme se vás na pár otázek na které musíte odpovědět.")
    Jmeno =  input("Jméno: ")
    Prijmeni = input("Přijmení: ")
    vek = input("Vek: ")
    if int(vek) > 18:
        volil = input("Volil jste? (ano/ne): ")
    if int(vek) < 18:
        volil = " "
    status = input("Jste svobodný? (ano/ne): ")
    print("Děkuji za vyplnění dotazníku. Nyní vypíšeme všechna data, která jsme o vás získali. Jestli je něco špatně, můžete ho udělat znova")
    print("")
    if volil == "ano" and status == "ano":
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,".format(vek) + "Jste svobodný a volil jste. Přeji vám hezký zbytek dne.")
    elif volil == "ne" and status == "ano":
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,"
              .format(vek) + "Jste svobodný a nevolil jste. Přeji vám hezký zbytek dne.")
    elif volil == "ano" and status == "ne":
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,"
              .format(vek) + "Nejste svobodný a volil jste. Přeji vám hezký zbytek dne.Určitě si někoho najdete.")
    elif volil == "ne" and status == "ne":
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,"
              .format(vek) + "nejste svobodný a nevolil jste. Přeji vám hezký zbytek dne.")
    elif volil == " " and status == "ano":
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,"
              .format(vek) + "Jste svobodný a jste moc mladý na volby. Děkujeme za dotazník.")
    elif volil == " " and status == "ne":
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,"
              .format(vek) + "Nejste svobodný a jste moc mladý na volby. Máte toho spoustu před sebou.")
    else:
        print("Jmenuje te se" + " " + Jmeno + " " + Prijmeni + " " + "je vám {} let,"
              .format(vek) + "Ohledně toho jestli jste svobodný,nebo jestli jste volili jste nám neřekl. Jsme smutni za vaši nedůvěru.")
    print("")
    pokracovat = input("Chcete tento dotazník vyplnit znovu?: (ano/ne)")