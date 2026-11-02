//////////////////////////////////////////////////////////////////////////////////////////
// Benchmark driver for the ATLAS Open Data ZBosonAnalysis selector (Zee sample only).
// Replaces main_ZBosonAnalysis.C so that the input path and the number of PROOF-Lite
// workers can be set from the command line. The selector itself is the unmodified
// upstream ZBosonAnalysis.C/.h.
//
//   nworkers == 1 : plain sequential TChain::Process (no PROOF)
//   nworkers >= 2 : PROOF-Lite with nworkers worker processes
//   nentries <= 0 : process all entries
//////////////////////////////////////////////////////////////////////////////////////////
#include "TChain.h"
#include "TEnv.h"
#include "TProof.h"
#include "TStopwatch.h"
#include "TTree.h"

void bench_Zee(const char* input, int nworkers = 1, const char* sandbox = "", Long64_t nentries = -1)
{
  TChain* chain = new TChain("mini");
  chain->AddFile(input);

  if (nworkers > 1) {
    // keep the PROOF sandbox (selector build cache, worker logs) on local scratch, not $HOME/.proof on AFS
    if (sandbox && sandbox[0]) gEnv->SetValue("ProofLite.Sandbox", sandbox);
    TProof::Open(TString::Format("workers=%d", nworkers));
    chain->SetProof();
  }

  Long64_t n = (nentries > 0) ? nentries : TTree::kMaxEntries;

  TStopwatch sw;
  sw.Start();
  chain->Process("ZBosonAnalysis.C+", "Zee", n);
  sw.Stop();
  printf("BENCH_LOOP_REALTIME %.3f\n", sw.RealTime());
  printf("BENCH_LOOP_CPUTIME %.3f\n", sw.CpuTime());
}
