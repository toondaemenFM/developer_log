# Reusable results

## UR + tool integration

:::{grid}
:::{grid-item-card} UR + tool integration
:link: https://github.com/Flanders-Make-vzw/ur_tool_integration

A reusable set of ROS2 packages that provide standard configurations for integration of a UR robot model with a custom tool.

**Target users:** {bdg-success}`developer` {bdg-success}`robotics integrator` {bdg-success}`non-robot expert`

**Tech stack:** {bdg-info}`ROS2` {bdg-info}`ROS2 launch` {bdg-info}`urdf` {bdg-info}`MoveIt`
:::

### Motivation
Setting up a robot configuration for [MoveIt](https://moveit.ai/) tends to be a challenging procedure, especially when additional assets -- like end-of-arm tooling for instance -- need to be added to the kinematic chain. Using the [MoveIt setup assistant tool](https://moveit.picknik.ai/main/doc/examples/setup_assistant/setup_assistant_tutorial.html), users can create their configuration, but the resulting configuration is ambiguous and scales poorly to very similar configurations that shouldn't require a reiteration of the entire configuration procedure. The flexibility is limited unless users edit the generated files afterwards, which requires users to have a decent understanding on [urdf](https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/URDF-Main.html) and how to navigate the generated packages.

This Reusable Result provides users a non-robotics expert user well-reasoned configuration that allows to easily set up a UR robot with a custom end-effector tool.

### Summary
The UR tool integration repository provides standard configurations for bringing up any robot from the [Universal Robots ecosystem](https://www.universal-robots.com/nl/) with a custom tool attached, for use within ROS2. It extends the existing robot models available from the [UR driver for ROS2](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver), and abstracts the robot configuration for the users to some .yaml files. The separate packages within this project are layered intentionally such that users can launch a configuration for their robot-with-tool setup, that suits their use case. All configurations can easily be validated using either a simulated or a physical robot. The README in the [Github repository](https://github.com/Flanders-Make-vzw/ur_tool_integration/tree/develop) can be considered as a tutorial that walks the user through the setup of the possible configurations, starting from the tool configuration itself, and ending at a fully functional configuration for collision-free trajectory planning and tracking with MoveIt.

```{figure} ./img/ur_tool_model.png
:alt: fig_ur_tool_model
:width: 100%
:name: fig_ur_tool_model
\: Integrated model of a UR robot and a custom tool
```

<br></br>
## The palletizing framework

The main result developed and validated in the [2024-1023-CTO_action_palletizing_solution](ref-project-palletizing-solution) was the palletizing framework: a ROS2-integrated framework for accommodating pallet solver plugins. The palletizing framework itself comes with a library of **MPLP** solvers: these address the **Manufacturer's Pallet Loading Problem**, where all boxes have the same size. These solvers can optimally stack the pallet following a certain pattern. Currently, two plugins are integrated as examples: *MPLP1* and *MPLP2*.

```{figure} ./img/mplp_1.png
:alt: fig_mplp_1
:width: 100%
:name: fig_mplp_1
\: Palletizing example using the integrated pallet solver **MPLP1**. Left: user interface and pallet visualisation in RVIZ. Right: stacking pattern applied by the pallet solver plugin.
```

```{figure} ./img/mplp_2.png
:alt: fig_mplp_2
:width: 100%
:name: fig_mplp_2
\: Palletizing example using the integrated pallet solver **MPLP2**. Left: user interface and pallet visualisation in RVIZ. Right: stacking pattern applied by the pallet solver plugin.
```

The [Ceros pallet solver](https://github.com/Flanders-Make-vzw/Ceros_Palletizing), developed in the scope of the CTO action addresses the **Distributor's Pallet Loading Problem (DPLP)**, where boxes have different sizes yet need to be optimally stacked. The solver algorithm was integrated as a pallet solver **plugin** for the palletizing framework as well, see the [demonstrator on mixed palletizing](ref-project-palletizing-solution).

:::{admonition} Potential
:class: admon-no-icon
The Palletizing framework architecture as result of the 2024-1023 CTO action is a starting point layout for the development of an integrated solution that generalizes the palletizing problem. Integrators that would take up this framework could elaborate on the framework by developing solver plugins on the one hand, and by elaborating on the capabilities of the framing around on the other hand.

Making it ready for open-source distribution in the ROS2-community is an option as well ofcourse.
::: 

:::{grid}
:::{grid-item-card} The palletizing framework
:link: https://github.com/Flanders-Make-vzw/2024-1023_CTO_action-palletizing_solution_framework

The implementation of the palletizing framework, built for accommodating pallet solver plugins. Includes the RVIZ plugins for pallet visualisation and the user interface to use the solvers. Includes an example library that implements two **mplp** solvers.

**Target users:** {bdg-success}`developer` {bdg-success}`robotics integrator`

**Tech stack:** {bdg-info}`C++` {bdg-info}`ROS2`
:::

<style>
    .admon-no-icon .admonition-title::before {content: "";}
</style>