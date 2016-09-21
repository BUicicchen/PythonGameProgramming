s = """Anzr: PvPv Pura
Rznvy: pvpvpura@cnpvsvpnzrevpna.bet
Tenqr: 11
Ylevpf bs fbat:
Fgnaq va gur yvtug naq or frra nf jr ner
Qvqa'g V gryy lbh V urne jung lbh fnl?
Arire ybbx onpx nf lbh'er jnyxvat njnl
Pneel gur zhfvp, gur zrzbevrf naq xrrc gurz vafvqr
Lbh
Ynhtu rirel qnl
Qba'g fgbc gubfr grnef sebz snyyvat
Qbja
Guvf vf jub V nz vafvqr
Guvf vf jub V nz, V'z abg tbvat gb uvqr
Pnhfr gur terngrfg evfx jr'yy rire gnxr vf ol sne
Gb fgnaq va gur yvtug naq or frra nf jr ner
Fb Fgnaq va gur yvtug naq or frra nf jr ner
"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
