from django.urls import include, path

from .views import usuario, players

urlpatterns = [
    path('', usuario.home, name='home'),


#    path('usuario/', include(([
 #       path('', students.QuizListView.as_view(), name='quiz_list'),
  #      path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
   #     path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
    #    path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
        

    path('players/', include(([
        path('', players.EventListView.as_view(), name='event_list'),
        path('interests/', players.PlayerInterestsView.as_view(), name='player_interests'), ], 'usuario'), namespace='players')),
    ]

