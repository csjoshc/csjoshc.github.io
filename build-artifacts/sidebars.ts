import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: "category",
      label: "Python",
      link: {
        type: "doc",
        id: "Python/base",
      },
      items: [
        {
          type: "category",
          label: "Data Science",
          link: {
            type: "doc",
            id: "Python/PythonforDataScience/Introduction",
          },
          items: [
            "Python/PythonforDataScience/Introduction",
            "Python/PythonforDataScience/Basics",
            "Python/PythonforDataScience/Numpy",
            "Python/PythonforDataScience/Pandas",
            "Python/PythonforDataScience/Pandas2",
            "Python/PythonforDataScience/Pandas3",
            "Python/PythonforDataScience/Pandas4",
            "Python/PythonforDataScience/Pandas5",
            "Python/PythonforDataScience/Matplotlib",
            "Python/PythonforDataScience/ML",
            "Python/PythonforDataScience/ML_Clust",
            "Python/PythonforDataScience/ML_DT",
            "Python/PythonforDataScience/ML_Reg",
          ],
        },
        {
          type: "category",
          label: "General Python",
          items: ["Python/General/virtenv_jupyter_nb"],
        },
        {
          type: "category",
          label: "Intro to Computer Science",
          items: [
            "Python/IntroCompThinkDataSci/unit1/unit1",
            "Python/IntroCompThinkDataSci/unit1/problemset1",
            "Python/IntroCompThinkDataSci/unit2/plotting",
            "Python/IntroCompThinkDataSci/unit2/unit2",
            "Python/IntroCompThinkDataSci/unit2/ps2",
            "Python/IntroCompThinkDataSci/unit3/unit3",
            "Python/IntroCompThinkDataSci/unit3/ps3",
            "Python/IntroCompThinkDataSci/unit4/unit4",
            "Python/IntroCompThinkDataSci/unit4/ps4",
            "Python/IntroCompThinkDataSci/unit5/unit5",
          ],
        },
        {
          type: "category",
          label: "Probability & Statistics",
          items: [
            "Python/ProbabilityandStatistics/Introduction",
            "Python/ProbabilityandStatistics/Sets",
          ],
        },
      ],
    },
    {
      type: "category",
      label: "General",
      link: {
        type: "doc",
        id: "General/base",
      },
      items: [
        "General/CS50x2019/cppbasics",
        "General/CS50x2019/webbasics",
        "General/CS50x2019/python",
        "General/CS50x2019/flask",
        "General/webdev2019",
      ],
    },
    {
      type: "category",
      label: "GitHub",
      link: {
        type: "doc",
        id: "Github/intro_gh",
      },
      items: ["Github/intro_gh"],
    },
    {
      type: "category",
      label: "Linux",
      link: {
        type: "doc",
        id: "Linux/base",
      },
      items: ["Linux/linux_journey/linux_journey_toc"],
    },
    {
      type: "category",
      label: "DevOps",
      link: {
        type: "doc",
        id: "Devops/base",
      },
      items: ["Devops/roadmap_notes"],
    },
    {
      type: "category",
      label: "Utilities",
      link: {
        type: "doc",
        id: "utils/base",
      },
      items: ["BatchConversions"],
    },
    {
      type: "category",
      label: "Site Updates",
      link: {
        type: "doc",
        id: "site_updates/base",
      },
      items: [
        "site_updates/6_2019/15_6_2019",
        "site_updates/6_2019/25_5_2019",
        "site_updates/5_2019/25_5_2019",
        "site_updates/5_2019/11_5_2019",
        "site_updates/5_2019/04_5_2019",
        "site_updates/4_2019/20_4_2019",
        "site_updates/4_2019/13_4_2019",
        "site_updates/3_2019/23_3_2019",
        "site_updates/3_2019/16_3_2019",
        "site_updates/3_2019/9_3_2019",
        "site_updates/3_2019/2_3_2019",
      ],
    },
    {
      type: "doc",
      id: "todo",
      label: "Todo",
    },
  ],
};

export default sidebars;
