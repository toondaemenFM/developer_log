# Projects overview

## 2024-2538-SIMROP
The SIMROP project facilitated the development of a skill--based programming framework. Several former projects within Flanders Make introduced the concept of skill--based programming for robotic applications, however a reusable and sustainable architecture and maintained implementation -- nor an aligned vision on the paradigm -- did not concretely exist.

The **SIMROP skill--based programming framework** aims to implement a contemporary interpretation of a platform for the development of modular, reusable and scalable robotic *skills*. The design leverages [ROS2](https://www.ros.org/) and [behavior trees](https://www.behaviortree.dev/) to compile a foundational architecture and reusable best-practice patterns for the development of intelligent and autonomous robotic systems.

**Conceptually**, the SIMROP skill--based framework is based on inquiring experiences with the use of [SkiROS2](https://github.com/RobotLabLTH/skiros2?tab=readme-ov-file), a skill--based programming framework developed by researchers at the universities of Lund (SW) and Copenhagen (DE). From an **Architecture** perspective, the implementation is heavily inspired on the software architecture of the [Navigation stack for ROS2](https://docs.nav2.org/).

The architecture is documented on the [SIMROP documentation page](https://flanders-make-vzw.github.io/2024-2835-SIMROP_Documentation), where also tutorials on the use of the framework can be found. Documentation and tutorials are under continuous development.

::::{grid} 2

:::{grid-item-card} SIMROP core architecture
:link: https://github.com/Flanders-Make-vzw/2024-2835-SIMROP_ROS2

The implementation of a reusable core architecture for building ROS2-based frameworks.

{bdg-info}`c++` {bdg-info}`ROS2` {bdg-info}`python`
:::

:::{grid-item-card} SIMROP skill-based framework
:link: https://github.com/Flanders-Make-vzw/2024-2835-SIMROP_SkillBasedSolution

The implementation of the SIMROP skill--based programming framework.
<br></br>

{bdg-info}`c++` {bdg-info}`ROS2` {bdg-info}`behavior trees`
:::

:::{grid-item-card} SIMROP release repository
:link: https://github.com/Flanders-Make-vzw/2024-2835-SIMROP_Release

Repository that releases Docker base images that contain the SIMROP core architecture and the SIMROP skill--based framework.

{bdg-info}`Docker`
:::

:::{grid-item-card} SIMROP documentation page
:link: https://flanders-make-vzw.github.io/2024-2835-SIMROP_Documentation

The documentation and tutorial page about the architecture and use of the SIMROP skill--based framework.
<br></br>

{bdg-info}`read-the-docs`
:::

::::

:::{admonition} Remark: framework name
:class: admon-no-icon
Currently, we're still looking for a suitable name that will permanently replace the working title **"SIMROP skill--based framework"**. We are looking for the right inspiration to come up with a decent and sustainable name that can be used while disseminating the framework. 
Personally, I am not in favour of acronyms, as they typically tend to be quite graceless. Often the acronym is first and then a meaning is hung onto it.
I am definitely not in favour of a name "devised" by an AI chatbot. I would prefer to find a good two- or three syllabe english term that refers to the notion of a *skill*, as in the meaning of a certain kind of *property* or *excellence*. I have been thinking about tree species and timber ypes, but actually the skill concepts is broader than purely the behavior trees. In that direction I didn't find something useful until now.
::: 

<br></br>
(ref-project-palletizing-solution)=
## 2024-1023-CTO_ACTION-PALLETIZING_SOLUTION

In the 2024-1023 CTO action, one of the goals was to work on the topic of **mixed palletizing**, or the [**Distributor's Pallet Loading Problem (DPLP)**](https://www.mdpi.com/2297-8747/26/3/53). A Heuristics based algorithm was developed at Flanders Make, addressing the problem of interest. Around the algorithm itself, a palletizing framework was developed, serving as an experimental environment to benchmark the performance of different algorithms, and anticipating industrial adoption. A physical scale model setup was built at Flanders Make where an industrial robot arm palletizes boxes that are supplied on a conveyor belt in order to practically validate and showcase the results provided by the algorithm implementations. The palletizing framework also anticipates the development of new pallet solvers, as the logic itself fits in the framework in de shape of a plugin.

Additionally, the robot in the physical demonstrater was integrated with [MoveIt](https://moveit.ai/), the motion planning and kinematics framework for ROS2. As the pallet itself is a dynamically growing obstacle for the robot, MoveIt allowed to perform collision free trajectories during palletizing.

```{figure} ./img/palletizing_demo.png
:alt: fig_palletizing_demo
:width: 100%
:name: fig_palletizing_demo
\: Integrated demonstration of the palletizing framework. Left: RVIZ plugin for visualisation of the result of the solver algorithm. Right: physical scale model demonstrator at Flanders Make
```

:::{admonition} Symposium demo
:class: admon-no-icon
See the [demonstrator in action](https://www.youtube.com/watch?v=0IojVjrQyFw) at the Flanders Make symposium 2024. 
:::

:::{grid}
:::{grid-item-card} The palletizing framework
:link: https://github.com/Flanders-Make-vzw/2024-1023_CTO_action-palletizing_solution_framework

The implementation of the palletizing framework, built for accommodating pallet solver plugins. Includes the RVIZ plugins for pallet visualisation and the user interface to use the solvers.

{bdg-info}`C++` {bdg-info}`ROS2`
:::

:::{grid-item-card} The palletizing framework
:link: https://github.com/Flanders-Make-vzw/Ceros_Palletizing

The implementation of the heuristics-based pallet solver.

{bdg-info}`Python` {bdg-info}`REST-api`
:::

::::


<style>
    .admon-no-icon .admonition-title::before {content: "";}
</style>