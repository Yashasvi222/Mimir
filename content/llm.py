import google.generativeai as genai
import time


def three_elements(top_corpus, model):
    tad_prompt = f"""
    **Top Corpus**: {top_corpus}
    From the Top corpus provided, extract just the author, title, year of the research paper in the form:  "Author||Title||Year"
    """

    response = model.generate_content(tad_prompt)
    return response.text


def zero_shot_learning(abstract, conclusion, model):
    zsl_findings_prompt = f"""
    You are an expert assistant in scientific literature analysis. Based on the abstract below, identify and summarize the key findings of the study. Aim to extract insights that highlight the study's main contributions and discoveries. Ensure that the response is concise yet covers all critical findings.
    
    **Abstract**: {abstract}
    
    **Key Findings**:
    """

    zsl_limitations_prompt = f"""
    You are an academic writing assistant focusing on summarizing research limitations. Based on the study's conclusion provided below, identify and summarize any limitations acknowledged by the authors or any potential limitations that might arise based on the conclusions. Aim for a brief, critical analysis that highlights areas where the research could improve.
    
    **Conclusion**: {conclusion}
    
    **Limitations**:
    """

    findings_response = model.generate_content(zsl_findings_prompt)
    limitations_response = model.generate_content(zsl_limitations_prompt)

    return findings_response.text, limitations_response.text


def one_shot_learning(abstract, conclusion, model):
    osl_findings_prompt = f"""
    You are an expert assistant in scientific literature analysis. Based on the abstract below, identify and summarize the key findings of the study. Aim to extract insights that highlight the study's main contributions and discoveries.
    
    **Example Abstract**: This study explores how machine learning improves forecasting accuracy in energy demand. It shows that machine learning models outperform traditional methods, providing real-time insights and more reliable predictions.
    
    **Example Findings**:
    1. Machine learning significantly improves accuracy in energy demand forecasting.
    2. The study shows that machine learning models can provide real-time insights, enhancing the reliability of predictions.
    
    **Abstract**: {abstract}
    
    **Key Findings**:
    """

    osl_limitations_prompt = f"""
    You are an academic writing assistant focusing on summarizing research limitations. Based on the study's conclusion provided below, identify and summarize any limitations acknowledged by the authors or potential limitations.
    
    **Example Conclusion**: This study provides insights into the benefits of machine learning for forecasting energy demand. However, the analysis relies solely on data from one year, potentially limiting its generalizability to other years.
    
    **Example Limitations**:
    1. The study’s reliance on data from one year limits generalizability to other timeframes.
    2. Future studies could improve accuracy by incorporating multi-year datasets.
    
    **Conclusion**: {conclusion}
    
    **Limitations**:
    """

    findings_response = model.generate_content(osl_findings_prompt)
    limitations_response = model.generate_content(osl_limitations_prompt)

    return findings_response.text, limitations_response.text


def few_shot_learning(abstract, conclusion, model):
    fsl_findings_prompt = f"""
    You are an expert assistant in scientific literature analysis. Based on the abstract below, identify and summarize the key findings of the study. Aim to extract insights that highlight the study's main contributions and discoveries.
    
    **Example Abstract 1**: This study explores how machine learning improves forecasting accuracy in energy demand. It shows that machine learning models outperform traditional methods, providing real-time insights and more reliable predictions.
    
    **Example Findings 1**:
    1. Machine learning significantly improves accuracy in energy demand forecasting.
    2. The study shows that machine learning models can provide real-time insights, enhancing the reliability of predictions.
    
    **Example Abstract 2**: The research investigates AI applications in healthcare diagnostics. Results indicate that AI tools improve diagnostic speed and accuracy compared to human-only methods, especially in radiology.
    
    **Example Findings 2**:
    1. AI tools in healthcare diagnostics enhance both speed and accuracy, particularly in radiology.
    2. AI demonstrates potential to reduce diagnostic errors when used alongside traditional methods.
    
    **Abstract**: {abstract}
    
    **Key Findings**:
    """
    fsl_limitations_prompt = f"""
    You are an academic writing assistant focusing on summarizing research limitations. Based on the study's conclusion provided below, identify and summarize any limitations acknowledged by the authors or potential limitations.
    
    **Example Conclusion 1**: This study provides insights into the benefits of machine learning for forecasting energy demand. However, the analysis relies solely on data from one year, potentially limiting its generalizability to other years.
    
    **Example Limitations 1**:
    1. The study’s reliance on data from one year limits generalizability to other timeframes.
    2. Future studies could improve accuracy by incorporating multi-year datasets.
    
    **Example Conclusion 2**: The research demonstrates the effectiveness of AI in healthcare diagnostics, focusing only on radiology data from a single hospital. This may limit the findings' applicability across other healthcare fields or institutions.
    
    **Example Limitations 2**:
    1. The study's focus on radiology data from one hospital may reduce generalizability to other healthcare settings.
    2. Broader studies across multiple fields and institutions are needed to verify these results.
    
    **Conclusion**: {conclusion}
    
    **Limitations**:
    """

    findings_response = model.generate_content(fsl_findings_prompt)
    limitations_response = model.generate_content(fsl_limitations_prompt)

    return findings_response.text, limitations_response.text


if __name__ == "__main__":
    ...
    # genai.configure(api_key="AIzaSyCrTcuC5KSq7CaeV_mSuuJkOIQgFcaxYrc")


    # corpus = """
    #     2015 5th Nirma University International Conference on Engineering (NUiCONE)
    #
    #
    # Development of Wireless Embedded Automation
    #
    #
    # System for Batch Process
    #
    #
    # Vivek Kadam, Sharad Jadhav, Mahesh Parihar, Amit Karande
    # Department of Instrumentation Engineering,
    # Ramrao Adik Institute of Technology, Nerul
    # Navi Mumbai, India.
    # vivekkadam1989@gmail.com, sharadpjadhav@gmail.com, parihar.rait@gmail.com
    # """
    # abstract = "Deep learning allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction. These methods have dramatically improved the state-of-the-art in speech recognition, visual object recognition, object detection and many other domains such as drug discovery and genomics. Deep learning discovers intricate structure in large data sets by using the backpropagation algorithm to indicate how a machine should change its internal parameters that are used to compute the representation in each layer from the representation in the previous layer. Deep convolutional nets have brought about breakthroughs in processing images, video, speech and audio, whereas recurrent nets have shone light on sequential data such as text and speech."
    # conclusion = "Unsupervised learning91–98 had a catalytic effect in reviving interest in deep learning, but has since been overshadowed by the successes of purely supervised learning. Although we have not focused on it in this Review, we expect unsupervised learning to become far more important in the longer term. Human and animal learning is largely unsupervised: we discover the structure of the world by observing it, not by being told the name of every object. Human vision is an active process that sequentially samples the optic array in an intelligent, task-specific way using a small, high-resolution fovea with a large, low-resolution surround. We expect much of the future progress in vision to come from systems that are trained end-toend and combine ConvNets with RNNs that use reinforcement learning to decide where to look. Systems combining deep learning and reinforcement learning are in their infancy, but they already outperform passive vision systems99 at classification tasks and produce impressive results in learning to play many different video games100. Natural language understanding is another area in which deep learning is poised to make a large impact over the next few years. We expect systems that use RNNs to understand sentences or whole documents will become much better when they learn strategies for selectively attending to one part at a time76,86. Ultimately, major progress in artificial intelligence will come about through systems that combine representation learning with complex reasoning. Although deep learning and simple reasoning have been used for speech and handwriting recognition for a long time, new paradigms are needed to replace rule-based manipulation of symbolic expressions by operations on large vectors"
    # # print(zero_shot_learning(abstract, conclusion)[0])
    # print(three_elements(corpus))
    # print("-" * 150)
    # time.sleep(1)
    # print(zero_shot_learning(abstract, conclusion)[0])
    # print("-" * 150)
    # time.sleep(1)
    # print(zero_shot_learning(abstract, conclusion)[1])
