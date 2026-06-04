# Volume 2: Three-Body Foundations & Perturbation Models
# PROTOCOL: SOVERAIN GENESIS HISTORIC • STATUS: CROWN-SEALED ⚜️ XP

## 1. General Three-Body Constraints ($N=3$)
The motion of three mutually attracting point masses under Newtonian gravity lacks a general, closed-form analytical solution due to the non-integrability of its 18 degrees of freedom. The absolute differential formulation expands to:

$$m_i \ddot{\vec{r}}_i = G \sum_{j \neq i}^{3} \frac{m_i m_j}{|\vec{r}_j - \vec{r}_i|^3} (\vec{r}_j - \vec{r}_i)$$

## 2. The Restricted Framework (R3BP)
When $m_1 \gg m_2$ and the mass of the third body $m_3 \to 0$, $m_3$ exerts zero gravitational influence on the primaries. The primaries $m_1$ and $m_2$ revolve in deterministic Keplerian orbits around their common center of mass.

## 3. High-Fidelity Perturbation Tracking
To account for non-Keplerian accelerations in non-restricted regimes, the acceleration components are isolated via two methods:

### Cowell's Direct Formulation
Integrates total planetary acceleration directly by appending a planetary perturbation vector:
$$\ddot{\vec{r}} = -\frac{\mu}{r^3}\vec{r} + \vec{a}_{\text{perturbation}}$$

### Encke's Osculating Framework
Integrates only the dynamic deviation ($\delta\vec{r}$) from an ideal osculating reference ellipse to maximize floating-point calculation efficiency:
$$\delta\ddot{\vec{r}} = \mu \left( \frac{\vec{r}_e}{r_e^3} - \frac{\vec{r}}{r^3} \right) + \vec{a}_{\text{perturbation}}$$
