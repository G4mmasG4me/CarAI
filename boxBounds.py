Fi = rotation

 H = w * Abs(Sin(Fi)) + h * Abs(Cos(Fi))
 W = w * Abs(Cos(Fi)) + h * Abs(Sin(Fi))
 as = Abs(Sin(Fi))
 cs = Abs(Cos(Fi))

 h = (H * cs - W * as) / (cs^2 - as^2)
 w = -(H * as - W * cs) / (cs^2 - as^2)

 XatTopEdge = w * cs      (AE at the picture)
 YatRightEdge = h * cs    (DH)
 XatBottomEdge = h * as   (BG)
 YatLeftEdge = w * as     (AF)
