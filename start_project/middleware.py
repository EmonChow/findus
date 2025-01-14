from django.http import JsonResponse
from django.urls import resolve
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class RoleBasedAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.unprotected_routes = [
            "login",
            "admin",
            "reset_password",
            "change_password_superadmin",
            "schema",
            "swagger-ui",
            "http://118.179.7.91/",
            
        ]

    def __call__(self, request):

        current_route = resolve(request.path_info).url_name

        if current_route in self.unprotected_routes or request.path.startswith(
            "/admin/"
        ):
            return self.get_response(request)

        # Manually authenticate the user using JWT authentication
        try:
            auth_result = JWTAuthentication().authenticate(request)
            if auth_result is None:
                return JsonResponse({"error": "Authentication required"}, status=401)

            # Unpack user and token
            user, _ = auth_result
        except AuthenticationFailed:
            return JsonResponse({"error": "Invalid token"}, status=401)

        # Get the user's role after successful authentication
        user_role = user.role.name

        role_based_access = {
            "STUDENT": [
                #  authentication module -> user urls
                "assessment_chart_by_student_id",
                "get_student_skillbased_assessments_by_student_id",
                "get_student_skillbased_writing_assessments_by_skillbased_assessment_id",
                "get_student_skillbased_assessment_result_summery",
                "all_student_textbook_by_student_id",
                "get_assessment_schedules_by_student_id",
                "all_skillbased_assessment_by_student_id",
                "get_student_textbook_assessments_by_textbook_id",
                "get_student_textbook_writing_assessments_by_textbook_assessments_id",
                "get_student_textbook_by_assessment_result_summery",
                "create_student_textbook_dictation",
                "get_student_textbook_dictation_by_dictaion_details_id",
                "get_student_textbook_dictation_result",
                "get_dictation_answer_by_details_id",
                "get_student_textbook_practicetest_by_practicetest_id",
                "get_student_textbook_practicetest_single",
                "submit_student_textbook_practicetest",
                "get_student_textbook_practicetest_by_practicetest_details_id",
                "fetch_practice_test_submitted_data_by_question_type",
                "get_student_practice_test_results",
                "get_student_practice_test_result_summery",
                "create_student_textbook_rop",
                "get_student_textbook_rop_by_practice_id",
                "create_student_textbook_video",
                "get_student_textbook_video_by_video_id",
                "all_school_subscription",
                "create_school_subscription",
                "update_school_subscription",
                "delete_school_subscription",
                "get_school_subscription",
                "all_school_subscription_without_pagination",
                "all_school_subscription_usage_history",
                "all_school_subscription_usage_history_by_id",
                "all_school_subscription_details_by_school_id",
                "search_school_subscription_usage_history",
                "get_school_details_by_school_code",
                #    student textbook
                "student_textbook_verification",
                "all_student_textbook",
                "all_student_textbook_by_school_id",
                "all_student_textbook_by_student_and_textbook_id",
                "get_student_textbook",
                "delete_student_textbook",
                "update_student_textbook",
                "create_student_textbook",
                #    student
                "all_student",
                "all_student_by_school_id",
                "create_student",
                "update_student",
                "delete_student",
                "student_bulk_upload",
                "get_student",
                "student_textbook_details",
                "get_textbook_details",
                "student_info",
                "update_student_class_info",
                #    textbook
                "all_textbook",
                "create_textbook",
                "update_textbook",
                "delete_textbook",
                "all_textbook_without_pagination",
                "get_textbook_details",
                "get_textbook",
                "search_textbook",
                #    textbook video
                "all_videos_by_texbookid_and_chapterid",
                "create_video",
                "update_video",
                "delete_video",
                "video_bulk_upload",
                "get_video",
                #    textbook chapter
                "all_textbook_chapter_by_texbookid",
                "create_textbook_chapter",
                "update_textbook_chapter",
                "delete_textbook_chapter",
                "get_textbook_chapter",
                #    practice test
                "all_practice_test_by_texbookid_and_chapterid",
                "get_practice_test",
                "create_practice_test",
                "update_practice_test",
                "delete_practice_test",
                #    dictation
                "all_dictation_by_texbookid_and_chapterid",
                "get_dictation",
                "create_dictation",
                "update_dictation",
                "delete_dictation",
                #    dictation question
                "get_dictation_questions",
                "create_dictation_question",
                "update_dictation_question",
                "delete_dictation_details",
                #    textbook writting assessment
                "all_textbook_writting_assessment",
                "all_textbook_writting_assessment_by_textbook_assessment",
                "delete_textbook_writting_assessment",
                "get_textbook_writting_assessment",
                "conduct_textbook_writing_assessment",
                "conduct_textbook_writing_assessment_result_show",
                "textbook_writing_assessment_conducted_result",
                "get_student_textbook_writing_assessment_result",
                "conduct_skillbased_writing_assessment",
                "conduct_skillbased_writing_assessment_result_show",
                "get_student_textbook_dictation_by_dictation_details_id",
                #reading out practice
                "get_reading_out_practice",
                "get_reading_out_practice_questions_by_practice_id",
                "get_skillbased_writting_assessment",
                "conduct_skillbased_writing_assessment_result_show_by_student",
                "grade_list",
                "superadminlist",
                "get_questionnaire_details",
                "create_student_questionnaries",
                "get_skillbased_writting_assessment_by_assessment_id_and_student_id",
                "get_textbook_writting_assessment_by_assessment_id_and_student_id",
                "get_student_questionaries_questions_id",
                "get_practicetest_question_type",
                "get_questionnary_chart_linear",
                "get_questionnary_chart_single",
                "activate_textbook_of_student",
                "conduct_textbook_speaking_assessment",
                "get_student_textbook_speaking_assessment_result_by_id",
                "get_student_textbook_speaking_assessment_result",
                "conduct_skillbased_speaking_assessment",
                "get_student_skillbased_speaking_assessment_result_by_id",
                "get_student_skillbased_speaking_assessment_result",
                "get_skillbased_speaking_assessment",
                "get_textbook_speaking_assessment",
                "get_student_practicetest_result_summery_for_student",
                "student_textbook_contents",
                "get_text_from_image_by_ocr",
                "get_a_video_progress",
              
            
            ],
            "SCHOOL": [
                #  authentication module -> user urls
                #    SCHOOL MODULES
                "get_skillbased_assessment_progress",
                "get_school_textbook_assessment_progress",
                "get_school_textbook_progress",
                "get_school_textbook_details",
                "rearrange_chapters",
                "validate-assessment-schedules",
                # school assessmnet schedule
                "get_school_assessment_schedule",
                "all_school_assessment_schedule_by_school_id",
                "create_school_assessment_schedule",
                "update_school_assessment_schedule",
                "search_textbook_assessment_by_textbook_id",
                "delete_school_assessment_schedule",
                # school profile urls
                "get_school_profiles_by_id",
                "get_school_assign_by_school_code",
                "search_school",
                #    CHECKME ADMIN MODULES
                # student profile urls
                "all_student_textbook_by_student_id",
                "get_assessment_schedules_by_student_id",
                "all_skillbased_assessment_by_student_id",
                #    student
                "all_student",
                "student_sorting_data",
                "all_student_by_school_id",
                "create_student",
                "update_student",
                "delete_student",
                "student_bulk_upload",
                "get_student",
                "activate_student",
                "deactivate_student",
                "list_of_deactivated_student",
                #    textbook
                "all_textbook",
                "create_textbook",
                "update_textbook",
                "delete_textbook",
                "all_textbook_without_pagination",
                "get_textbook_details",
                "get_textbook",
                "search_textbook",
                #    textbook video
                "all_videos_by_texbookid_and_chapterid",
                "create_video",
                "update_video",
                "delete_video",
                "video_bulk_upload",
                "get_video",
                #    textbook chapter
                "all_textbook_chapter_by_texbookid",
                "create_textbook_chapter",
                "update_textbook_chapter",
                "delete_textbook_chapter",
                "get_textbook_chapter",
                #    student textbook
                "student_textbook_verification",
                "all_student_textbook",
                "all_student_textbook_by_school_id",
                "all_student_textbook_by_student_and_textbook_id",
                "get_student_textbook",
                "delete_student_textbook",
                "update_student_textbook",
                "create_student_textbook",
                #    textbook assessment
                "all_textbook_assessment",
                "create_textbook_assessment",
                "update_textbook_assessment",
                "delete_textbook_assessment",
                "get_textbook_assessment",
                "get_textbook_assessment_by_textbook_id",
                #    textbook writting assessment
                "all_textbook_writting_assessment",
                "all_textbook_writting_assessment_by_textbook_assessment",
                "create_textbook_writting_assessment",
                "update_textbook_writting_assessment",
                "delete_textbook_writting_assessment",
                "get_textbook_writting_assessment",
                #    skillbased assessment
                "all_skillbased_assessment",
                "create_skillbased_assessment",
                "update_skillbased_assessment",
                "delete_skillbased_assessment",
                "get_skillbased_assessment",
              
                #    skill based writting assessment
                "all_skillbased_writting_assessment",
                "create_skillbased_writting_assessment",
                "update_skillbased_writting_assessment",
                "delete_skillbased_writting_assessment",
                "get_skillbased_writting_assessment",
                "get_skillbased_writting_assessment_by_skillbased_assessment",
                #    schools
                "all_schools",
                "all_schools_without_pagination",
                #    school subscription
                "all_school_subscription",
                "create_school_subscription",
                "update_school_subscription",
                "delete_school_subscription",
                "get_school_subscription",
                "all_school_subscription_without_pagination",
                "all_school_subscription_usage_history",
                "all_school_subscription_usage_history_by_id",
                "all_school_subscription_details_by_school_id",
                "search_school_subscription_usage_history",
                "get_school_details_by_school_code",
                #    reading out practice
                "upload_audio_url",
                "get_reading_out_practice",
                "all_reading_out_practice_by_texbookid_and_chapterid",
                "get_reading_out_practice_response",
                "create_reading_out_practice",
                "update_reading_out_practice",
                "delete_reading_out_practice",
                "readingout_practice_question_bulk_upload",
                #    reading out practice questions
                "get_reading_out_practice_questions_by_practice_id",
                "update_reading_out_practice_questions",
                "delete_reading_out_practice_questions",
                #    practicetest questions
                "create_practicetest_questions",
                "update_practicetest_questions",
                "get_practicetest_questions",
                "get_practicetest_questions_by_practicetest_id",
                "delete_practicetest_question",
                #    practice test
                "all_practice_test_by_texbookid_and_chapterid",
                "get_practice_test",
                "create_practice_test",
                "update_practice_test",
                "delete_practice_test",
                #    dictation
                "all_dictation_by_texbookid_and_chapterid",
                "get_dictation",
                "create_dictation",
                "update_dictation",
                "delete_dictation",
                #    dictation question
                "get_dictation_questions",
                "create_dictation_question",
                "update_dictation_question",
                "delete_dictation_details",
                "generate_student_pdf",
                "search_student",
                "get_student_textbook_assessments_by_textbook_id",
                "get_student_textbook_writing_assessments_by_textbook_assessments_id",
                "get_student_textbook_by_assessment_result_summery",
                "get_student_textbook_practicetest_by_practicetest_id",
                "get_student_textbook_practicetest_single",
                "submit_student_textbook_practicetest",
                "get_student_textbook_practicetest_by_practicetest_details_id",
                "fetch_practice_test_submitted_data_by_question_type",
                "get_student_practice_test_results",
                "get_student_practice_test_result_summery",
                "get_student_skillbased_assessment_result_summery",
                #school
                "school_dashboard_data",
                "school_dashboard_details_data",
                "rearrange_textbook_assessment",
                "rearrange_skillbased_assessment",
                "rearrange_video",
                "rearrange_dictation_question",
                "rearrange_dictation",
                "rearrange_reading_out_practice",
                "rearrange_reading_out_practice_questions",
                "grade_list",
                "permanent_delete_student",
                "superadminlist",
                "archived_student_list",
                "restore_student",
                "update_school_subscription_number_of_students",
                "chapter-progress",
                "get_questionnary_student_data",
                # "student_textbook_details",
                "get_student_skillbased_speaking_assessment_result",
                "get_student_textbook_speaking_assessment_result",
                "update_textbook_writting_assessment_type",
                "update_skillbased_writting_assessment_type",
             
             
                
            ],
            "ADMIN": [
                #  authentication module -> user urls
                #    SCHOOL MODULES
                # school assessmnet schedule
                "admin_dashboard_chart",
                "get_skillbased_assessment_progress",
                "get_school_textbook_assessment_progress",
                "get_school_textbook_progress",
                "change_school_password",
                "update_school",
                "a_school",
                "get_school_assessment_schedule",
                "all_school_assessment_schedule_by_school_id",
                "create_school_assessment_schedule",
                "update_school_assessment_schedule",
                "search_textbook_assessment_by_textbook_id",
                # school profile urls
                "get_school_profiles_by_id",
                "get_school_assign_by_school_code",
                "search_school",
                #    CHECKME ADMIN MODULES
                # student profile urls
                "all_student_textbook_by_student_id",
                "get_assessment_schedules_by_student_id",
                "all_skillbased_assessment_by_student_id",
                #    student
                "all_student",
                "all_student_by_school_id",
                "create_student",
                "update_student",
                "delete_student",
                "student_bulk_upload",
                "get_student",
                "permanent_delete_student",

                #    textbook
                "all_textbook",
                "create_textbook",
                "update_textbook",
                "delete_textbook",
                "all_textbook_without_pagination",
                "get_textbook_details",
                "get_textbook",
                "search_textbook",
                #    textbook video
                "all_videos_by_texbookid_and_chapterid",
                "create_video",
                "update_video",
                "delete_video",
                "video_bulk_upload",
                "get_video",
                #    textbook chapter
                "all_textbook_chapter_by_texbookid",
                "create_textbook_chapter",
                "update_textbook_chapter",
                "delete_textbook_chapter",
                "rearrange_chapters",
                "rearrange_skillbased_assessment",
                "get_textbook_chapter",
                #    student textbook
                "student_textbook_verification",
                "all_student_textbook",
                "all_student_textbook_by_school_id",
                "all_student_textbook_by_student_and_textbook_id",
                "get_student_textbook",
                "delete_student_textbook",
                "update_student_textbook",
                "create_student_textbook",
                #    textbook assessment
                "all_textbook_assessment",
                "create_textbook_assessment",
                "update_textbook_assessment",
                "delete_textbook_assessment",
                "get_textbook_assessment",
                "get_textbook_assessment_by_textbook_id",
                #    textbook writting assessment
                "all_textbook_writting_assessment",
                "all_textbook_writting_assessment_by_textbook_assessment",
                "create_textbook_writting_assessment",
                "update_textbook_writting_assessment",
                "delete_textbook_writting_assessment",
                "get_textbook_writting_assessment",
                #    skillbased assessment
                "all_skillbased_assessment",
                "create_skillbased_assessment",
                "update_skillbased_assessment",
                "delete_skillbased_assessment",
                "get_skillbased_assessment",
                "rearrange_textbook_assessment",
                "rearrange_practice_tests",
                #    skill based writting assessment
                "all_skillbased_writting_assessment",
                "create_skillbased_writting_assessment",
                "update_skillbased_writting_assessment",
                "delete_skillbased_writting_assessment",
                "get_skillbased_writting_assessment",
                "get_skillbased_writting_assessment_by_skillbased_assessment",
                #    schools
                "all_schools",
                "all_schools_without_pagination",
                #    school subscription
                "all_school_subscription",
                "create_school_subscription",
                "update_school_subscription",
                "delete_school_subscription",
                "get_school_subscription",
                "all_school_subscription_without_pagination",
                "all_school_subscription_usage_history",
                "all_school_subscription_usage_history_by_id",
                "all_school_subscription_details_by_school_id",
                "search_school_subscription_usage_history",
                "get_school_details_by_school_code",
                #    reading out practice
                "upload_audio_url",
                "get_reading_out_practice",
                "all_reading_out_practice_by_texbookid_and_chapterid",
                "get_reading_out_practice_response",
                "create_reading_out_practice",
                "update_reading_out_practice",
                "readingout_practice_question_bulk_upload",
                "delete_reading_out_practice",
                #    reading out practice questions
                "get_reading_out_practice_questions_by_practice_id",
                "update_reading_out_practice_questions",
                "delete_reading_out_practice_questions",
                #    practicetest questions
                "create_practicetest_questions",
                "update_practicetest_questions",
                "get_practicetest_questions",
                "get_practicetest_questions_by_practicetest_id",
                "delete_practicetest_question",
                #    practice test
                "all_practice_test_by_texbookid_and_chapterid",
                "get_practice_test",
                "create_practice_test",
                "update_practice_test",
                "delete_practice_test",
                #    dictation
                "all_dictation_by_texbookid_and_chapterid",
                "get_dictation",
                "create_dictation",
                "update_dictation",
                "delete_dictation",
                #    dictation question
                "get_dictation_questions",
                "create_dictation_question",
                "update_dictation_question",
                "delete_dictation_details",
                "generate_student_pdf",
                "search_student",
                #dashboard
                "admin_dashboard_data",
                "dashboard_school_report",
                "dashboard_student_report",
                "rearrange_video",
                "rearrange_dictation_question",
                "rearrange_dictation",
                "rearrange_reading_out_practice",
                "rearrange_reading_out_practice_questions",
                "validate-assessment-schedules",
                "grade_list",
                "superadminlist",
                "superadmin",
                "createsuperadmin",
                "updatesuperadmin",
                "deletesuperadmin",
                "restore_textbook",
                "archived_textbook_list",
                "restore_textbook_chapter",
                "archived_textbook_chapter_list",
                "restore_video",
                "archived_video_list",
                "restore_reading_out_practice",
                "archived_reading_out_practice_list",
                "restore_dictation",
                "archived_dictation_list", 
                "restore_practice_test", 
                "archived_practice_test_list",
                "restore_textbook_assessment",
                "archived_textbook_assessment_list",
                "restore_skillbased",
                "archived_skillbased_assessment_list",
                "restore_skillbased_writing_assessment",
                 "restore_textbook_based_writing_assessment",
                "archived_skillbased_writing_assessment_list",
                "archived_textbook_based_writing_assessment_list",
                "restore_student",
                "archived_student_list",
                "create_questionnaries" ,
                "update_questionnaries" ,
                "delete_questionnaries" ,
                "all_questionnaries" ,
                "get_questionnaries_by_id",
                "create_questionnaries_details",
                "duplicate_questionnaries_details",
                "update_questionnaries_details",
                "delete_questionnaries_details",
                "get_questionnaries_details",
                "all_questionnaries_details_by_questionnaries_id",
                "rearrange_questionnaries_details",
               
                
                "permanent_delete_textbook",
                "permanent_delete_video",
                "permanent_delete_textbook_writting_assessment",
                "permanent_delete_textbook_chapter",
                "permanent_delete_textbook_assessment",
                "permanent_delete_skillbased_writting_assessment",
                "permanent_delete_skillbased_assessment",
                "permanent_delete_reading_out_practice",
                "permanent_delete_practice_test",
                "permanent_delete_dictation",
                "check_textbook_exists",
                "all_questionnaries_details",
                "get_questionnary_chart_linear",
                "get_questionnary_chart_single",
                "get_questionnary_student_data",
                "all_questionnaries_with_params",
                "get_questionnary_chart",
                "delete_student_questionnaires",
                "create_student_questionnaries",
                "update_school_subscription_number_of_students",
                "create_textbook_speaking_assessment",
                "get_textbook_speaking_assessment",
                "all_textbook_speaking_assessment_by_textbook_assessment",
                "get_textbook_speaking_assessment",
                "update_textbook_speaking_assessment",
                "delete_textbook_speaking_assessment",
                "all_textbook_speaking_assessment",
                "search_school_questionnaries",
                
                
                
                "all_skillbased_speaking_assessment",
                "get_skillbased_speaking_assessment",
                "get_skillbased_speaking_assessment_by_skillbased_assessment",
                "create_skillbased_speaking_assessment",
                "update_skillbased_speaking_assessment",
                "delete_skillbased_speaking_assessment",
                "permanent_delete_textbook_speaking_assessment",
                
                "restore_textbook_based_speaking_assessment",
                "archived_textbook_based_speaking_assessment_list",
                "restore_skillbased_speaking_assessment",
                "archived_skillbased_speaking_assessment_list",
                "show_in_excel_questionniare_data",
                "permanent_delete_skillbased_speaking_assessment",
                                                
                                
              
               
            ],
        }

        # Check if the current role has access to the route
        if user_role in role_based_access:
            allowed_routes = role_based_access[user_role]

            if current_route in allowed_routes:

                response = self.get_response(request)
                return response
            else:

                print(f"Access denied for {user_role} to {current_route}")
                return JsonResponse(
                    {"error": "Access denied for this role"}, status=403
                )
        else:
            return JsonResponse({"error": "Role not authorized"}, status=403)
