#Salaam testing

epsilon = 2
maxid = 0
with open('livejournal-undirected.txt') as infile:
    for line in infile:
        line = line.strip()
        ids = line.split("\t")
        maxid = max(maxid,int(ids[0]),int(ids[1]))
S = ones(maxid+1)
Stilde = ones(maxid+1)
inducedsetsize = 0
degrees = zeros(maxid+1)
with open('livejournal-undirected.txt') as infile:
    for line in infile:
        line = line.strip()
        ids = line.split("\t")
        inducedsetsize = inducedsetsize+1
        degrees[int(ids[0])] = degrees[int(ids[0])] + 1
        degrees[int(ids[1])] = degrees[int(ids[1])] + 1
rho = float(inducedsetsize)/sum(S)
Sizes=[]
edgeSizes=[]
rhos=[]
Sizes.append(sum(S))
edgeSizes.append(inducedsetsize)
rhos.append(rho)
for i in range(0,maxid+1):
    if S[i]==1:
        if degrees[i] <= (2*(1+epsilon)*rho):
            S[i]=0
rhoold = rho
iterno = 1
while sum(S)>0:
    iterno = iterno + 1
    degrees = zeros(maxid+1)
    inducedsetsize = 0
    with open('livejournal-undirected.txt') as infile:
        for line in infile:
            line = line.strip()
            ids = line.split("\t")
            if S[int(ids[0])]==1 and S[int(ids[1])]==1:
                inducedsetsize = inducedsetsize+1
                degrees[int(ids[0])] = degrees[int(ids[0])] + 1
                degrees[int(ids[1])] = degrees[int(ids[1])] + 1
    rho = float(inducedsetsize)/sum(S)
    edgeSizes.append(inducedsetsize)
    Sizes.append(sum(S))
    rhos.append(rho)
    if rho > rhoold:
        Stilde = list(S)
        rhoold = rho
    for i in range(0,maxid+1):
        if S[i]==1:
            if degrees[i] <= 2*(1+epsilon)*rho:
                S[i]=0

Sizes.append(0)
edgeSizes.append(0)
print('|S|:')
print(Sizes)
print('|E(S)|:')
print(edgeSizes)
print('rho:')
print(rhos)
print('Number of Iteration:')
print(iterno)

iterationsone = np.arange(iterno+1)
plot(iterationsone,Sizes)
xlabel('Iteration')
ylabel('|S|')
fig2 = figure()
plot(iterationsone,edgeSizes)
xlabel('Iteration')
ylabel('|E(S)|')
iterationstwo = np.arange(iterno)
fig3 = figure()
plot(iterationstwo,rhos)
xlabel('Iteration')
ylabel('rho(S)')
