#!/usr/bin/env python3

import GoL_SAT_utils

def gen_SL (center, a):
    s="(!a||!b||!c||!q||!d)&&(!a||!b||!c||!q||!e)&&(!a||!b||!c||!q||!f)&&" \
      "(!a||!b||!c||!q||!g)&&(!a||!b||!c||!q||!h)&&(!a||!b||!c||q||d||e||f||g||h)&&" \
      "(!a||!b||c||q||!d||e||f||g||h)&&(!a||!b||c||q||d||!e||f||g||h)&&" \
      "(!a||!b||c||q||d||e||!f||g||h)&&(!a||!b||c||q||d||e||f||!g||h)&&" \
      "(!a||!b||c||q||d||e||f||g||!h)&&(!a||!b||!q||!d||!e)&&(!a||!b||!q||!d||!f)&&" \
      "(!a||!b||!q||!d||!g)&&(!a||!b||!q||!d||!h)&&(!a||!b||!q||!e||!f)&&" \
      "(!a||!b||!q||!e||!g)&&(!a||!b||!q||!e||!h)&&(!a||!b||!q||!f||!g)&&" \
      "(!a||!b||!q||!f||!h)&&(!a||!b||!q||!g||!h)&&(!a||b||!c||q||!d||e||f||g||h)&&" \
      "(!a||b||!c||q||d||!e||f||g||h)&&(!a||b||!c||q||d||e||!f||g||h)&&" \
      "(!a||b||!c||q||d||e||f||!g||h)&&(!a||b||!c||q||d||e||f||g||!h)&&" \
      "(!a||b||c||q||!d||!e||f||g||h)&&(!a||b||c||q||!d||e||!f||g||h)&&" \
      "(!a||b||c||q||!d||e||f||!g||h)&&(!a||b||c||q||!d||e||f||g||!h)&&" \
      "(!a||b||c||q||d||!e||!f||g||h)&&(!a||b||c||q||d||!e||f||!g||h)&&" \
      "(!a||b||c||q||d||!e||f||g||!h)&&(!a||b||c||q||d||e||!f||!g||h)&&" \
      "(!a||b||c||q||d||e||!f||g||!h)&&(!a||b||c||q||d||e||f||!g||!h)&&" \
      "(!a||!c||!q||!d||!e)&&(!a||!c||!q||!d||!f)&&(!a||!c||!q||!d||!g)&&" \
      "(!a||!c||!q||!d||!h)&&(!a||!c||!q||!e||!f)&&(!a||!c||!q||!e||!g)&&" \
      "(!a||!c||!q||!e||!h)&&(!a||!c||!q||!f||!g)&&(!a||!c||!q||!f||!h)&&" \
      "(!a||!c||!q||!g||!h)&&(!a||!q||!d||!e||!f)&&(!a||!q||!d||!e||!g)&&" \
      "(!a||!q||!d||!e||!h)&&(!a||!q||!d||!f||!g)&&(!a||!q||!d||!f||!h)&&" \
      "(!a||!q||!d||!g||!h)&&(!a||!q||!e||!f||!g)&&(!a||!q||!e||!f||!h)&&" \
      "(!a||!q||!e||!g||!h)&&(!a||!q||!f||!g||!h)&&(a||!b||!c||q||!d||e||f||g||h)&&" \
      "(a||!b||!c||q||d||!e||f||g||h)&&(a||!b||!c||q||d||e||!f||g||h)&&" \
      "(a||!b||!c||q||d||e||f||!g||h)&&(a||!b||!c||q||d||e||f||g||!h)&&" \
      "(a||!b||c||q||!d||!e||f||g||h)&&(a||!b||c||q||!d||e||!f||g||h)&&" \
      "(a||!b||c||q||!d||e||f||!g||h)&&(a||!b||c||q||!d||e||f||g||!h)&&" \
      "(a||!b||c||q||d||!e||!f||g||h)&&(a||!b||c||q||d||!e||f||!g||h)&&" \
      "(a||!b||c||q||d||!e||f||g||!h)&&(a||!b||c||q||d||e||!f||!g||h)&&" \
      "(a||!b||c||q||d||e||!f||g||!h)&&(a||!b||c||q||d||e||f||!g||!h)&&" \
      "(a||b||!c||q||!d||!e||f||g||h)&&(a||b||!c||q||!d||e||!f||g||h)&&" \
      "(a||b||!c||q||!d||e||f||!g||h)&&(a||b||!c||q||!d||e||f||g||!h)&&" \
      "(a||b||!c||q||d||!e||!f||g||h)&&(a||b||!c||q||d||!e||f||!g||h)&&" \
      "(a||b||!c||q||d||!e||f||g||!h)&&(a||b||!c||q||d||e||!f||!g||h)&&" \
      "(a||b||!c||q||d||e||!f||g||!h)&&(a||b||!c||q||d||e||f||!g||!h)&&" \
      "(a||b||c||!q||d||e||f||g)&&(a||b||c||!q||d||e||f||h)&&" \
      "(a||b||c||!q||d||e||g||h)&&(a||b||c||!q||d||f||g||h)&&" \
      "(a||b||c||!q||e||f||g||h)&&(a||b||c||q||!d||!e||!f||g||h)&&" \
      "(a||b||c||q||!d||!e||f||!g||h)&&(a||b||c||q||!d||!e||f||g||!h)&&" \
      "(a||b||c||q||!d||e||!f||!g||h)&&(a||b||c||q||!d||e||!f||g||!h)&&" \
      "(a||b||c||q||!d||e||f||!g||!h)&&(a||b||c||q||d||!e||!f||!g||h)&&" \
      "(a||b||c||q||d||!e||!f||g||!h)&&(a||b||c||q||d||!e||f||!g||!h)&&" \
      "(a||b||c||q||d||e||!f||!g||!h)&&(a||b||!q||d||e||f||g||h)&&" \
      "(a||c||!q||d||e||f||g||h)&&(!b||!c||!q||!d||!e)&&(!b||!c||!q||!d||!f)&&" \
      "(!b||!c||!q||!d||!g)&&(!b||!c||!q||!d||!h)&&(!b||!c||!q||!e||!f)&&" \
      "(!b||!c||!q||!e||!g)&&(!b||!c||!q||!e||!h)&&(!b||!c||!q||!f||!g)&&" \
      "(!b||!c||!q||!f||!h)&&(!b||!c||!q||!g||!h)&&(!b||!q||!d||!e||!f)&&" \
      "(!b||!q||!d||!e||!g)&&(!b||!q||!d||!e||!h)&&(!b||!q||!d||!f||!g)&&" \
      "(!b||!q||!d||!f||!h)&&(!b||!q||!d||!g||!h)&&(!b||!q||!e||!f||!g)&&" \
      "(!b||!q||!e||!f||!h)&&(!b||!q||!e||!g||!h)&&(!b||!q||!f||!g||!h)&&" \
      "(b||c||!q||d||e||f||g||h)&&(!c||!q||!d||!e||!f)&&(!c||!q||!d||!e||!g)&&" \
      "(!c||!q||!d||!e||!h)&&(!c||!q||!d||!f||!g)&&(!c||!q||!d||!f||!h)&&" \
      "(!c||!q||!d||!g||!h)&&(!c||!q||!e||!f||!g)&&(!c||!q||!e||!f||!h)&&" \
      "(!c||!q||!e||!g||!h)&&(!c||!q||!f||!g||!h)&&(!q||!d||!e||!f||!g)&&" \
      "(!q||!d||!e||!f||!h)&&(!q||!d||!e||!g||!h)&&(!q||!d||!f||!g||!h)&&" \
      "(!q||!e||!f||!g||!h)"

    d={"q":center, "a":a[0], "b":a[1], "c":a[2], "d":a[3], "e":a[4], "f":a[5], "g":a[6], "h":a[7]}
    return GoL_SAT_utils.mathematica_to_CNF(s, d)

