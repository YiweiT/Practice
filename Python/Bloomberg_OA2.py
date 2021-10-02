# During election, every citizens is voting through voting machine. 
# This machine calls your API function with (candidateID, voterID).
# Write this function to return top 5 candidates after every vote.
# Also report a fraud if a voter tries to vote twice of different candidates
# For ties, sort by candidateID

# global variables
past_vote = {} # {voteid, candidateid}
candidates = [] # [[candidateID, cnt]] index means the rank
# vote = [candidateID, voterID]
def voteAPI(vote: List[int]):
    candidateID, voterID = vote[0], vote[1]
    # first check whether the given voter has already voted for someone
    if voterID in past_vote:
        if candidateID != past_vote[voterID]:
            # the given voter has already voted for a different candidate before
            print('Fraud!')
            return
        else:
            # the given voter has already voted for the same candidate before
            print('You have voted for the same candidate before.')
    else:
        # for the new voter, add the voter and voted candidate to past_vote dict
        past_vote[voterID] = candidateID
        # calculate the top 5 candidates based on their voters' count
        if candidateID in past_vote.values():
            candidates[candidateID] += 1
        else:
            candidates.append([candidateID, 1])

    return None
voteAPI([1, 23])