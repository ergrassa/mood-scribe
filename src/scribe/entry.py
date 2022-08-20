import matplotlib.pyplot as plt
from io import BytesIO
import base64
from scribe.emo import *

def plot_entry(entry):
    ks = entry.keys()
    vs = list(map(int,entry.values()))
    cs = [{v==1: '#d43', v==2: '#ca4', v==3: '#ac4', v==5: '#6d8', v==8: '#9df'}[True] for v in vs]
    fig, ax = plt.subplots()
    # fig.set_facecolor((1.0, 1.0, 1.0, 0.3))
    fig.patch.set_facecolor('w')
    fig.patch.set_alpha(0.3)
    fig.set_size_inches(12,5)
    ax.bar(ks, vs, color=cs)
    ax.set_ylim(0, 8.5)
    ax.set_yticks([1,2,3,5,8])
    ax.patch.set_facecolor('w')
    ax.patch.set_alpha(0.0)
    pfile = BytesIO()
    fig.savefig(pfile, format='png', bbox_inches='tight')
    pfile.seek(0)
    efile = base64.b64encode(pfile.getvalue())
    efile = efile.decode('utf-8')
    return efile

def plot_history(df):
    fig, ax = plt.subplots()
    # df.set_index('datetime')
    offset = -0.2
    for c in cols:
        df[c] = df[c].astype(int)
        df[c] = df[c].apply(lambda x: x+offset)
        offset += 0.1
    df.plot(x='datetime', ax=ax)
    fig.patch.set_facecolor('w')
    fig.patch.set_alpha(0.3)
    fig.set_size_inches(12,5)
    ax.set_ylim(0, 8.5)
    ax.set_yticks([1,2,3,5,8])
    ax.patch.set_facecolor('w')
    ax.patch.set_alpha(0.0)
    pfile = BytesIO()
    fig.savefig(pfile, format='png', bbox_inches='tight')
    pfile.seek(0)
    efile = base64.b64encode(pfile.getvalue())
    efile = efile.decode('utf-8')
    return efile