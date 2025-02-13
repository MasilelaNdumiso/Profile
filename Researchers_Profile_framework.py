# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:46:15 2025

@author: MasilelaNd
"""

import streamlit as st

st.title("Researchers Profile")

st.markdown("I am a dedicated and detail-oriented Hydrologist with a strong foundation in the National Water Act (Act 36 of 1998) with over three years of experience in South Africa’s national water monitoring programs. My expertise includes performance monitoring, drought risk management, and data management for the National Integrated Water Information System (NIWIS). I am a Professional Natural Scientist (SACNASP), proficient in hydrological modeling and flow routing using MIKE+ Rivers, MODFLOW, and HEC-RAS for water resources system operations, Geographical Information Systems, Satellite-based Remote Sensing, and advanced data management using R-Scripts and Python programming languages. My experience includes processing, analyzing, and interpreting various hydrological and spatial data, including expertise in High-Performance Computing (HPC) for large-scale data analysis. Additionally, I have co-authored peer-reviewed publications contributing to hydrological drought monitoring and groundwater assessment in South Africa.")


tab1, tab2, tab3= st.tabs(["About", "Publications", "Current projects"])
                                                               

#%%
#make the pages