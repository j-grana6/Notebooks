(* Content-type: application/vnd.wolfram.cdf.text *)

(*** Wolfram CDF File ***)
(* http://www.wolfram.com/cdf *)

(* CreatedBy='Mathematica 9.0' *)

(*************************************************************************)
(*                                                                       *)
(*  The Mathematica License under which this file was created prohibits  *)
(*  restricting third parties in receipt of this file from republishing  *)
(*  or redistributing it by any means, including but not limited to      *)
(*  rights management or terms of use, without the express consent of    *)
(*  Wolfram Research, Inc. For additional information concerning CDF     *)
(*  licensing and redistribution see:                                    *)
(*                                                                       *)
(*        www.wolfram.com/cdf/adopting-cdf/licensing-options.html        *)
(*                                                                       *)
(*************************************************************************)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[      1063,         20]
NotebookDataLength[      8914,        187]
NotebookOptionsPosition[      9272,        176]
NotebookOutlinePosition[      9849,        199]
CellTagsIndexPosition[      9806,        196]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{

Cell[CellGroupData[{
Cell[BoxData[""], "Input", "PluginEmbeddedContent"],

Cell[BoxData[
 TagBox[
  StyleBox[
   DynamicModuleBox[{$CellContext`gamma$$ = 5, $CellContext`rover$$ = 
    5.13, $CellContext`runder$$ = 1, $CellContext`Z$$ = 1, Typeset`show$$ = 
    True, Typeset`bookmarkList$$ = {}, Typeset`bookmarkMode$$ = "Menu", 
    Typeset`animator$$, Typeset`animvar$$ = 1, Typeset`name$$ = 
    "\"untitled\"", Typeset`specs$$ = {{{
       Hold[$CellContext`rover$$], 5, 
       Style["High Reserve Price," OverBar[$CellContext`r], 18]}, 0.01, 10}, {{
       Hold[$CellContext`runder$$], 1, 
       Style["Low Reserve Price," UnderBar[$CellContext`r], 18]}, 0.01, 10}, {{
       Hold[$CellContext`Z$$], 1, 
       Style[
       "Rate of Information Acquisition," (
         Subscript[$CellContext`\[Lambda], 1] + 
         Subscript[$CellContext`\[Lambda], 2]), 18]}, 0.01, 10}, {{
       Hold[$CellContext`gamma$$], 5, 
       Style["Rate of Demand Shocks," $CellContext`\[Gamma], 18]}, 0.01, 10}},
     Typeset`size$$ = {360., {182., 190.}}, Typeset`update$$ = 0, 
    Typeset`initDone$$, Typeset`skipInitDone$$ = 
    True, $CellContext`rover$189597$$ = 0, $CellContext`runder$189598$$ = 
    0, $CellContext`Z$189599$$ = 0, $CellContext`gamma$189600$$ = 0}, 
    DynamicBox[Manipulate`ManipulateBoxes[
     1, StandardForm, 
      "Variables" :> {$CellContext`gamma$$ = 5, $CellContext`rover$$ = 
        5, $CellContext`runder$$ = 1, $CellContext`Z$$ = 1}, 
      "ControllerVariables" :> {
        Hold[$CellContext`rover$$, $CellContext`rover$189597$$, 0], 
        Hold[$CellContext`runder$$, $CellContext`runder$189598$$, 0], 
        Hold[$CellContext`Z$$, $CellContext`Z$189599$$, 0], 
        Hold[$CellContext`gamma$$, $CellContext`gamma$189600$$, 0]}, 
      "OtherVariables" :> {
       Typeset`show$$, Typeset`bookmarkList$$, Typeset`bookmarkMode$$, 
        Typeset`animator$$, Typeset`animvar$$, Typeset`name$$, 
        Typeset`specs$$, Typeset`size$$, Typeset`update$$, Typeset`initDone$$,
         Typeset`skipInitDone$$}, "Body" :> RegionPlot[
        And[(-($CellContext`delta + 
             2 $CellContext`gamma$$)) ($CellContext`delta - $CellContext`mu) \
($CellContext`delta + 
            2 $CellContext`gamma$$ + $CellContext`mu) ($CellContext`delta \
($CellContext`delta + 
              2 $CellContext`gamma$$) + ($CellContext`delta + \
$CellContext`gamma$$) $CellContext`mu) $CellContext`runder$$ + \
($CellContext`gamma$$ $CellContext`mu ($CellContext`delta + \
$CellContext`gamma$$ + $CellContext`mu) (
              2 ($CellContext`delta + $CellContext`gamma$$) + \
$CellContext`mu) $CellContext`rover$$ + ((-$CellContext`delta) \
($CellContext`delta + 2 $CellContext`gamma$$)^2 (3 $CellContext`delta + 
                2 $CellContext`gamma$$) - ($CellContext`delta - 
               2 $CellContext`gamma$$) ($CellContext`delta + \
$CellContext`gamma$$) ($CellContext`delta + 
               2 $CellContext`gamma$$) $CellContext`mu + (
                3 $CellContext`delta^2 + 
                8 $CellContext`delta $CellContext`gamma$$ + 
                6 $CellContext`gamma$$^2) $CellContext`mu^2 + \
($CellContext`delta + $CellContext`gamma$$) $CellContext`mu^3) \
$CellContext`runder$$) $CellContext`Z$$ + ($CellContext`gamma$$ \
$CellContext`mu (3 ($CellContext`delta + $CellContext`gamma$$) + 
              2 $CellContext`mu) $CellContext`rover$$ - (3 $CellContext`delta + 
             4 $CellContext`gamma$$ + 
             2 $CellContext`mu) ($CellContext`delta ($CellContext`delta + 
               2 $CellContext`gamma$$) - ($CellContext`delta + \
$CellContext`gamma$$) $CellContext`mu) $CellContext`runder$$) \
$CellContext`Z$$^2 + ($CellContext`gamma$$ $CellContext`mu \
$CellContext`rover$$ + ((-$CellContext`delta) ($CellContext`delta + 
                2 $CellContext`gamma$$) + ($CellContext`delta + \
$CellContext`gamma$$) $CellContext`mu) $CellContext`runder$$) \
$CellContext`Z$$^3 > 
         0, (-$CellContext`delta^5) $CellContext`rover$$ - \
$CellContext`delta^4 $CellContext`rover$$ (
           5 $CellContext`gamma$$ + $CellContext`mu + 
           3 $CellContext`Z$$) - $CellContext`delta^3 (
           8 $CellContext`gamma$$^2 $CellContext`rover$$ + 
           4 $CellContext`gamma$$ $CellContext`mu $CellContext`rover$$ - \
$CellContext`mu^2 $CellContext`rover$$ - $CellContext`gamma$$ $CellContext`mu \
$CellContext`runder$$ + (
             12 $CellContext`gamma$$ + $CellContext`mu) $CellContext`rover$$ \
$CellContext`Z$$ + 
           3 $CellContext`rover$$ $CellContext`Z$$^2) + $CellContext`delta \
($CellContext`mu $CellContext`rover$$ $CellContext`Z$$ ($CellContext`mu + \
$CellContext`Z$$)^2 + 
            4 $CellContext`gamma$$^3 ($CellContext`mu $CellContext`runder$$ - \
$CellContext`rover$$ $CellContext`Z$$) + 
            2 $CellContext`gamma$$^2 ($CellContext`mu^2 ($CellContext`rover$$ + 
                3 $CellContext`runder$$) + 
              4 $CellContext`mu $CellContext`runder$$ $CellContext`Z$$ - 
              3 $CellContext`rover$$ $CellContext`Z$$^2) + \
$CellContext`gamma$$ ($CellContext`mu + $CellContext`Z$$) ($CellContext`mu^2 (
                2 $CellContext`rover$$ + $CellContext`runder$$) + \
$CellContext`mu (4 $CellContext`rover$$ + 
                3 $CellContext`runder$$) $CellContext`Z$$ - 
              2 $CellContext`rover$$ $CellContext`Z$$^2)) - \
$CellContext`delta^2 (4 $CellContext`gamma$$^3 $CellContext`rover$$ + 
           2 $CellContext`gamma$$^2 (
             2 $CellContext`mu ($CellContext`rover$$ - $CellContext`runder$$) + 
             7 $CellContext`rover$$ $CellContext`Z$$) - $CellContext`rover$$ \
($CellContext`mu + $CellContext`Z$$) ($CellContext`mu^2 + 
            2 $CellContext`mu $CellContext`Z$$ - $CellContext`Z$$^2) + \
$CellContext`gamma$$ ((-$CellContext`mu^2) (3 $CellContext`rover$$ + 
               2 $CellContext`runder$$) + 
             3 $CellContext`mu ($CellContext`rover$$ - $CellContext`runder$$) \
$CellContext`Z$$ + 
             9 $CellContext`rover$$ $CellContext`Z$$^2)) + \
$CellContext`gamma$$ $CellContext`mu (
            2 $CellContext`gamma$$ + $CellContext`mu + $CellContext`Z$$) \
(($CellContext`rover$$ + $CellContext`runder$$) $CellContext`Z$$ \
($CellContext`mu + $CellContext`Z$$) + $CellContext`gamma$$ \
($CellContext`rover$$ $CellContext`Z$$ + 
              2 $CellContext`runder$$ ($CellContext`mu + $CellContext`Z$$))) > 
         0], {$CellContext`mu, 0.01, 10}, {$CellContext`delta, 0.01, 5}, 
        FrameLabel -> {
         "Rate of Public Information,  \[Mu]", " Discount Rate,  \[Delta]"}, 
        BaseStyle -> {FontSize -> 18}], 
      "Specifications" :> {{{$CellContext`rover$$, 5, 
          Style["High Reserve Price," OverBar[$CellContext`r], 18]}, 0.01, 10,
          Appearance -> "Labeled"}, {{$CellContext`runder$$, 1, 
          Style["Low Reserve Price," UnderBar[$CellContext`r], 18]}, 0.01, 10,
          Appearance -> "Labeled"}, {{$CellContext`Z$$, 1, 
          Style[
          "Rate of Information Acquisition," (
            Subscript[$CellContext`\[Lambda], 1] + 
            Subscript[$CellContext`\[Lambda], 2]), 18]}, 0.01, 10, Appearance -> 
         "Labeled"}, {{$CellContext`gamma$$, 5, 
          Style["Rate of Demand Shocks," $CellContext`\[Gamma], 18]}, 0.01, 
         10, Appearance -> "Labeled"}}, 
      "Options" :> {ControlPlacement -> Right}, "DefaultOptions" :> {}],
     ImageSizeCache->{1002., {215., 220.}},
     SingleEvaluation->True],
    Deinitialization:>None,
    DynamicModuleValues:>{},
    SynchronousInitialization->True,
    UnsavedVariables:>{Typeset`initDone$$},
    UntrackedVariables:>{Typeset`size$$}], "Manipulate",
   Deployed->True,
   StripOnInput->False],
  Manipulate`InterpretManipulate[1]]], "Output", "PluginEmbeddedContent"]
}, Open  ]]
},
WindowSize->{1066, 466},
WindowMargins->{{418, Automatic}, {Automatic, 239}},
Visible->True,
AuthoredSize->{1066.3600000000001`, 466.11},
ScrollingOptions->{"HorizontalScrollRange"->Fit,
"VerticalScrollRange"->Fit},
ShowCellBracket->False,
Deployed->True,
CellContext->Notebook,
TrackCellChangeTimes->False,
FrontEndVersion->"9.0 for Microsoft Windows (64-bit) (January 25, 2013)",
StyleDefinitions->"Default.nb"
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[CellGroupData[{
Cell[1485, 35, 51, 0, 16, "Input"],
Cell[1539, 37, 7717, 136, 437, "Output"]
}, Open  ]]
}
]
*)

(* End of internal cache information *)

(* NotebookSignature SwTxGkROdFlI@D17fvHvxZ3A *)
