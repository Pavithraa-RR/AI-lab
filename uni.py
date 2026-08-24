def unify(x,y,subst={}):
    if x == y:
        return subst
    elif isinstance(x,str) and x.islower():
        return {x:y}
    elif isinstance(y,str) and y.islower():
        return {x:y}
    else:
        return none
    def resolve(c1, c2):
        for lit1 in c1:
            for lit2 in c2:
                if lit1 == "~"+lit2 or "~"+ lit1 == lit2:
                    new_clause = list(set(c1+c2) - {lit1,lit2})
                    retuennew_clause
                    return none
                def resolution(kb, query):
                    claused = kb + [["~"+q for q in query]]
                while true:
                    new_clause =[]
                    for i in range(len(clause)):
                        for j in range(i+1, len(clauses)):
                            resolvent = resolvet(clauses[i], clauses[j])
                            if resolvent is not none:
                                if not reasolvent:
                                    return true
                                new_clauses.append(resolvent)
                                if not any(c1 not in clauses for c1 in new_clauses):
                                    return false
                                clauses.extend(new_clauses)
                                kb=[
                                    ["P(a)"],
                                    ["~P(a)", "Q(a)"]
                                    ]
                                query = ["Q(a)"]
                                if resolution(kb, query):
                                    print("query os entailed by the knowlwdge base")
                                else:
                                    print("query is nor entailed by the knowledge base")
                                        





                                                                                                                                                                                                              
